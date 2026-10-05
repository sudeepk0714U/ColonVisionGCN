from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = ROOT_DIR / "archive"
DATA_DIR = ROOT_DIR / "data"

RESULTS_DIR = ROOT_DIR / "results"

MODEL_DIR = RESULTS_DIR / "models"
EMBEDDING_DIR = RESULTS_DIR / "embeddings"
GRAPH_DIR = RESULTS_DIR / "graphs"
PLOT_DIR = RESULTS_DIR / "plots"
GRADCAM_DIR = RESULTS_DIR / "gradcam"


# ============================================================
# DATASET
# ============================================================

CLASSES = [
    "dyed-lifted-polyps",
    "dyed-resection-margins",
    "normal-cecum",
    "normal-z-line",
    "polyps",
    "ulcerative-colitis"
]

NUM_CLASSES = len(CLASSES)

CLASS_TO_INDEX = {
    class_name: index
    for index, class_name in enumerate(CLASSES)
}

INDEX_TO_CLASS = {
    index: class_name
    for class_name, index in CLASS_TO_INDEX.items()
}


# ============================================================
# IMAGE
# ============================================================

IMAGE_SIZE = 224


# ============================================================
# TRAINING
# ============================================================

BATCH_SIZE = 4

NUM_EPOCHS = 15

LEARNING_RATE = 1e-4

WEIGHT_DECAY = 1e-4

NUM_WORKERS = 0


# ============================================================
# GRAPH
# ============================================================

K_NEIGHBORS = 10

EPSILON = 0.35

PCA_COMPONENTS = 256


# ============================================================
# RANDOM SEED
# ============================================================

RANDOM_SEED = 42