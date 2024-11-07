# Local Image Search System using CLIP
This project is a local image search system powered by OpenAI's CLIP (Contrastive Language–Image Pretraining) model. It allows users to upload a folder of images and query the system with text descriptions. The model then returns the images that best match the provided query, based on semantic similarity.
![Screenshot 2024-11-07 233646](https://github.com/user-attachments/assets/07785d0e-51e0-412d-98f1-9d7a6a9667f9)
## Features
- Folder Upload: Upload a folder containing multiple images.
- Text-Based Image Search: Query the uploaded images using descriptive text to find the most relevant images.
- Semantic Similarity: Uses CLIP's vision-language capabilities to match text prompts with images based on their content, rather than just metadata or filenames.
## Setup
### Prerequisites
  - Python 3.8 or higher
  - CUDA for GPU acceleration (optional but recommended)
  - Virtual Environment (recommended)
    
### Installation
  **1. Clone the Repository:**
  ```bash
     git clone https://github.com/yourusername/stable-diffusion-inpainting.git
     cd stable-diffusion-inpainting
  ```
  **2. Create and Activate Virtual Environment:**
  ```bash
     conda create -n env python=3.11
     conda activate env
  ```
  **3. Install Required Packages:**
  ```bash
     pip install -r requirements.txt
  ```
### Usage
**1. Run the Application:**
  ```bash
    python app.py
   ```
**2. Upload Folder:** Once the application is running, upload a folder of images you want to search through.
**3. Provide a Query Prompt:** Enter a text description to search for images related to your prompt (e.g., "A dog running in the park").
**4. View Results:** The system will display the images most similar to your query, ranked by relevance.

## How It Works
- Image Embedding: When the image folder is uploaded, each image is encoded into an embedding vector using CLIP's image encoder.
- Query Embedding: The input text query is converted into an embedding vector using CLIP's text encoder.
- Similarity Matching: Cosine similarity is used to compare the query embedding with each image embedding. Images with the highest similarity scores are returned as the best matches.

## Acknowledgments
- [research paper](https://arxiv.org/abs/2103.00020)
