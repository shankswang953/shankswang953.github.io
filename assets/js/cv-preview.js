import { getDocument, GlobalWorkerOptions } from "../lib/pdfjs-5.6.205/pdf.min.mjs";

GlobalWorkerOptions.workerSrc = new URL(
  "../lib/pdfjs-5.6.205/pdf.worker.min.mjs",
  import.meta.url
).href;

const preview = document.querySelector(".cv-preview[data-pdf-url]");

if (preview) {
  const status = preview.querySelector(".cv-preview__status");

  try {
    const pdfDocument = await getDocument({
      url: preview.dataset.pdfUrl,
      isEvalSupported: false,
      useWasm: false,
    }).promise;
    const pages = document.createDocumentFragment();

    for (let number = 1; number <= pdfDocument.numPages; number += 1) {
      const page = await pdfDocument.getPage(number);
      const original = page.getViewport({ scale: 1 });
      const viewport = page.getViewport({ scale: 1500 / original.width });
      const canvas = document.createElement("canvas");
      canvas.width = Math.ceil(viewport.width);
      canvas.height = Math.ceil(viewport.height);
      canvas.setAttribute("role", "img");
      canvas.setAttribute("aria-label", `CV page ${number} of ${pdfDocument.numPages}`);

      await page.render({ canvas, viewport }).promise;

      const sheet = document.createElement("div");
      sheet.className = "cv-preview__page";
      sheet.appendChild(canvas);
      pages.appendChild(sheet);
      page.cleanup();
    }

    preview.replaceChildren(pages);
  } catch (error) {
    status.textContent = "Please use the download link above to read the CV.";
    console.error("Unable to render the CV preview:", error);
  } finally {
    preview.setAttribute("aria-busy", "false");
  }
}
