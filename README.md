# RapidOCR-PreOCR

[English](#english) | [中文](#chinese) 

機械翻訳 | Maschinelle Übersetzung | Traduction automatique | Traducción Automática |

[日本語](#japanese) | [Deutsch](#deutsch) | [Français](#francais) | [Español](#espanol)

---

<a name="english"></a>
## English
**RapidOCR-PreOCR** is an image preprocessing tool specifically optimized for **scanned medical reports**. It addresses critical issues such as line-skipping and broken-line recognition in RapidOCR, significantly enhancing text continuity and data integrity.

In medical scenarios (e.g., lab results, clinical summaries), OCR often fails due to thin fonts, low contrast, or uneven scanning quality. By integrating **CLAHE** (Contrast Limited Adaptive Histogram Equalization) and fine-tuned denoising, this tool strengthens the structural features of text. This ensures that RapidOCR can reliably extract every line of vital medical information where high precision is non-negotiable.

---

<a name="chinese"></a>
## 中文
**RapidOCR-PreOCR** 是一款专为优化 **医学报告扫描件** 识别效果而设计的图像预处理工具。它主要解决在特定场景下出现的漏行、断行等问题，显著提升文本识别的连续性与完整性。

在处理医疗化验单、出院小结等扫描文档时，由于字体较细、对比度较低或光线不均，常规 OCR 往往会丢失关键行。本项目通过 **CLAHE**（限制对比度自适应直方图均衡化）与优化去噪算法，强化文字结构特征，确保 RapidOCR 能够稳健地捕获每一行医疗关键信息，极大地提高了数据提取的可靠性。

---

<a name="japanese"></a>
## 日本語 (機械翻訳)
**RapidOCR-PreOCR** は、**医療報告書の教細なスキャンデータ**に特化した画像前処理ツールです。RapidOCR で発生しやすい「行飛ばし」や「文字の断裂」といった課題を解決し、テキスト認識の連続性とデータ整合性を大幅に向上させます。

診断書や検査結果などの医療現場では、フォントの細さやコントラストの低さにより、通常の OCR では重要な行を見落とすことがあります。本プロジェクトでは **CLAHE** とノイズ除去を組み合わせることで、文字の構造的特徴を強化し、精度が求められる医療情報の確実な抽出を支援します。

---

<a name="deutsch"></a>
## Deutsch (Maschinelle Übersetzung)
**RapidOCR-PreOCR** ist ein Bildvorverarbeitungswerkzeug, das speziell für **gescannte medizinische Berichte** optimiert wurde. Es löst kritische Probleme wie das Überspringen von Zeilen und die Erkennung unterbrochener Linien in RapidOCR, wodurch die Textkontinuität und Datenintegrität erheblich verbessert werden.

In medizinischen Szenarien (z. B. Laborergebnisse, klinische Zusammenfassungen) scheitert OCR oft an dünnen Schriftarten, geringem Kontrast oder ungleichmäßiger Scanqualität. Durch die Integration von **CLAHE** und fein abgestimmter Rauschunterdrückung stärkt dieses Tool die strukturellen Merkmale von Texten und gewährleistet eine präzise Extraktion wichtiger medizinischer Informationen.

---

<a name="francais"></a>
## Français (Traduction Automatique)
**RapidOCR-PreOCR** est un outil de prétraitement d'image spécifiquement optimisé pour les **rapports médicaux numérisés**. Il résout des problèmes critiques tels que le saut de lignes et la reconnaissance de lignes brisées dans RapidOCR, améliorant considérablement la continuité du texte et l'intégrité des données.

Dans les contextes médicaux (ex: résultats de laboratoire, comptes rendus cliniques), l'OCR échoue souvent en raison de polices fines, d'un faible contraste ou d'une qualité de numérisation inégale. En intégrant la technologie **CLAHE** et une réduction du bruit optimisée, cet outil renforce les caractéristiques structurelles du texte, garantissant une extraction fidèle des informations médicales vitales.

---

<a name="espanol"></a>
## Español (Traducción Automática)
**RapidOCR-PreOCR** es una herramienta de preprocesamiento de imágenes optimizada específicamente para **informes médicos escaneados**. Resuelve problemas críticos como el salto de líneas y el reconocimiento de líneas fragmentadas en RapidOCR, mejorando significativamente la continuidad del texto y la integridad de los datos.

En entornos médicos (ej. resultados de laboratorio, resúmenes clínicos), el OCR suele fallar debido a fuentes delgadas, bajo contraste o calidad de escaneo desigual. Al integrar **CLAHE** y una reducción de ruido optimizada, esta herramienta fortalece las características estructurales del texto, garantizando una extracción fiel de información médica vital.

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
