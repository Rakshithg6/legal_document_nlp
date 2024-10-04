try:
    import torch
    print("PyTorch version:", torch.__version__)
except ImportError:
    print("PyTorch is not installed.")

try:
    import tensorflow as tf
    print("TensorFlow version:", tf.__version__)
except ImportError:
    print("TensorFlow is not installed.")
