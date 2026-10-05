# ColonXAI

## Explainable Colon Disease Classification Using Vision Transformers and Graph Convolutional Networks

ColonXAI is a deep learning project for automated classification of colonoscopy images into six gastrointestinal disease and anatomical classes.

The project combines a **Vision Transformer (ViT)** for visual feature extraction with a **Graph Convolutional Network (GCN)** for graph-based classification. The extracted image representations are converted into a k-nearest-neighbor graph, allowing the GCN to learn relationships between visually similar colonoscopy images.

The project also aims to incorporate **Grad-CAM++** for visual explainability, helping identify the image regions contributing to the model's predictions.

---

## Project Overview

Colonoscopy images can contain visually similar patterns across different diseases and anatomical regions. Conventional image classification models treat each image independently, whereas graph-based learning can model relationships between samples.

ColonXAI follows a two-stage learning pipeline:

```text
                    Colonoscopy Image
                           │
                           ▼
                  Vision Transformer
                        (ViT)
                           │
                           ▼
                  192-D Feature Vector
                           │
                           ▼
                  k-NN Graph Construction
                           │
                           ▼
                 Graph Convolutional
                    Network (GCN)
                           │
                           ▼
                 6-Class Classification
                           │
                           ▼
                     Prediction
                           │
                           ▼
                      Grad-CAM++
                  Explainable Prediction