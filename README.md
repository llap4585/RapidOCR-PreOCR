# RapidOCR-PreOCR

**RapidOCR-PreOCR** is an image preprocessing tool designed to address line-skipping or broken-line issues in RapidOCR under certain scenarios, significantly improving text continuity recognition.

In practical applications, such as processing scanned medical reports or laboratory results, traditional OCR often struggles with thin fonts, uneven scanning lighting, or low contrast, leading to critical data loss or fragmented lines. 
By applying CLAHE (Contrast Limited Adaptive Histogram Equalization) and optimized denoising, this tool enhances the structural features of text, ensuring that RapidOCR can accurately capture every line of vital medical information with much higher reliability.


## References / Citation
```markdown
This project builds upon the RapidOCR toolbox. If you use RapidOCR, please cite:

@misc{RapidOCR2021,
    title={{Rapid OCR}: OCR Toolbox},
    author={RapidAI Team},
    howpublished = {\url{https://github.com/RapidAI/RapidOCR}},
    year={2021}
}

If you use this project, please cite it as:

@misc{llap4585,
    title={RapidOCR-PreOCR: Preprocessing tool for improved RapidOCR text continuity},
    author={llap4585},
    howpublished = {\url{https://github.com/llap4585/RapidOCR-PreOCR}},
    year={2026}
}
