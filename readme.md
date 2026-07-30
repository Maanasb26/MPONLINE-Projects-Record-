# **MP – Online – AIML Projects** 

### **Name: Maanas Brahme** 

**Reg no: 23BCE10567 Application no:** **<mark>IN26010827 Batch : 1A</mark>** 

# **<mark>Project Details</mark>** 

## **1. Adult Census** 

Predicts whether an individual's annual income exceeds **$50K** based on census data. Compares **5 classifiers** (Logistic Regression, Decision Tree, Random Forest, KNN, SVM) on metrics like Accuracy, Precision, Recall, F1, and ROC-AUC. 

**Dataset:** Adult Census Income Dataset (Kaggle) — ~32,561 records, 14 features **Pipeline:** Data Cleaning → Feature Engineering (One-Hot, StandardScaler) → Model Training → Evaluation 

## **<mark>2. Cancer Classifcation</mark>** 

Classifies brain MRI images into **4 categories** (Glioma, Meningioma, No Tumor, Pituitary) using a custom **3-block CNN** with BatchNorm, Dropout, and data augmentation. Targets **90%+ accuracy** . 

**Dataset:** Brain Tumor MRI Dataset (Kaggle) — 5,600 training + 1,600 test images **Architecture:** 3 × Conv blocks (32→64→128) + GlobalAveragePooling + EarlyStopping 

## **<mark>3. Placement Predictor</mark>** 

Predicts the Placement probability of Students based on Metrices like CGPA, Skills, Aptitude and 10<sup>th</sup> and 12<sup>Th</sup> Grades 

**Live Demo:** <u>https://student-placement-predictor-docker-yog6.onrender.com</u> 

**Features:** Present Price, Kms Driven, Fuel Type, Transmission, Car Age, etc. **Deployment:** Flask + Pickle → Render 

## **<mark>4. CIFAR 10</mark>** 

Classifies **32×32 RGB images** into **10 object categories** (Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, Truck) using a custom CNN with data augmentation. Targets **85%+ accuracy** . 

**Dataset:** CIFAR-10 — 50,000 training + 10,000 test images (loaded via TensorFlow) 

**Architecture:** 3 × Conv blocks (32→64→128) + Flatten + Dense + ReduceLROnPlateau 

## **<mark>5. LFW Face Recognition</mark>** 

Recognizes **faces of 7 public figures** from the Labeled Faces in the Wild dataset using a custom CNN. Handles limited training data through augmentation and stratified splitting. 

**Dataset:** LFW — 1,288 grayscale images (50×37), 7 classes (loaded via scikitlearn) 

**Architecture:** 3 × Conv blocks (32→64→128) + EarlyStopping (patience=20) 

## **<mark>6. Movie Recommendation System</mark>** 

A content-based movie recommendation engine using **TF-IDF Vectorization** and **Cosine Similarity** on movie genres. Served through a clean **Flask web interface** . 

**Dataset:** TMDB Movie Dataset 

**Live Demo:** <u>https://movie-recommendation-system-i7g3.onrender.com</u> 

**Pipeline:** TF-IDF on genres → Cosine Similarity matrix → Top-N recommendations 

## **7. Document AI – RAG Chatbot** 

An End to End Retrieval Augmented Generation Chatbot where you can upload any PDF document and Ask Questions regarding the context 

**Stack:** FastAPI + Sentence-Transformers (MiniLM) + FAISS (vector search) + Gemini AI 

**Live Demo:** <u>https://documind-ai-ii0p.onrender.com</u> 

**Flow:** Embed query → FAISS similarity search → Top-k excerpts → Gemini generates grounded answer 

## **<mark>8. CARTPOLE – Reinforcement Learning</mark>** 

Trains an agent to balance a pole on a cart using **Proximal Policy Optimization (PPO)** with Stable-Baselines3 in the Gymnasium CartPole-v1 environment. 

**Framework:** Stable-Baselines3, Gymnasium 

**Components:** train.py, evaluate.py, test.py, record_video.py, plot_training.py 

## **<mark>9. Lunar Landing Simulation – Reinforcement Learning</mark>** 

Trains an autonomous spacecraft agent to safely land on a designated pad using **Deep Q-Network (DQN)** with the Box2D physics simulator. 

**Framework:** Stable-Baselines3, Gymnasium (LunarLander-v3) **Components:** train.py, evaluate.py, test.py, record_video.py, plot_training.py 

# **<mark>Technologies Used</mark>** 

|**Category**|**Tools & Libraries**|
|---|---|
|**Languages**|Python 3|
|**ML / DL**|Scikit-learn, TensorFlow / Keras|
|**RL**|Stable-Baselines3, Gymnasium|
|**NLP / RAG**|TF-IDF, Sentence-Transformers, FAISS, Gemini AI|
|**Web**|Flask, FastAPI|
|**Data**|Pandas, NumPy|
|**Visualization**|Matplotlib, Seaborn|
|**Deployment**|Render, Pickle|
|**Environment**|Jupyter Notebook, VS Code|



