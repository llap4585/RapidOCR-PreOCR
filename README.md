# RapidOCR-PreOCR

[English](#english) | [中文](#chinese)| [日本語（機械翻訳）](#japanese)

---

<a name="english"></a>
## English
**RapidOCR-PreOCR** is an image preprocessing tool specifically optimized for **scanned medical reports**. It addresses critical issues such as line-skipping and broken-line recognition in RapidOCR, significantly enhancing text continuity and data integrity.

In medical scenarios (e.g., lab results, clinical summaries), OCR often fails due to thin fonts, low contrast, or uneven scanning quality. By integrating **CLAHE** (Contrast Limited Adaptive Histogram Equalization) and fine-tuned denoising, this tool strengthens the structural features of text. This ensures that RapidOCR can reliably extract every line of vital medical information where high precision is non-negotiable.

---

<a name="chinese"></a>
## 中文说明
**RapidOCR-PreOCR** 是一款专为优化 **医学报告扫描件** 识别效果而设计的图像预处理工具。它主要解决在特定场景下出现的漏行、断行等问题，显著提升文本识别的连续性与完整性。

在处理医疗化验单、出院小结等扫描文档时，由于字体较细、对比度较低或光线不均，常规 OCR 往往会丢失关键行。本项目通过 **CLAHE**（限制对比度自适应直方图均衡化）与优化去噪算法，强化文字结构特征，确保 RapidOCR 能够稳健地捕获每一行医疗关键信息，极大地提高了数据提取的可靠性。

---

<a name="japanese"></a>
## 日本語 (Machine Translation)
**RapidOCR-PreOCR** は、**医療報告書の教細なスキャンデータ**に特化した画像前処理ツールです。RapidOCR で発生しやすい「行飛ばし」や「文字の断裂」といった課題を解決し、テキスト認識の連続性とデータ整合性を大幅に向上させます。

診断書や検査結果などの医療現場では、フォントの細さやコントラストの低さにより、通常の OCR では重要な行を見落とすことがあります。本プロジェクトでは **CLAHE** とノイズ除去を組み合わせることで、文字の構造的特徴を強化し、精度が求められる医療情報の確実な抽出を支援します。

---
## 🛠️ Requirements

```text
opencv-python
rapidocr_onnxruntime
```
---

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
