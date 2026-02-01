# AI in Machine Assembling
### Predictive Maintenance using Machine Learning

## 📌 Overview
This repository contains our research work **“AI in Machine Assembling”**, which focuses on applying Artificial Intelligence and Machine Learning techniques for predictive maintenance in industrial manufacturing systems. The project aims to predict machine failures in CNC milling operations using sensor and operational data, enabling proactive maintenance and reduced unplanned downtime.

---

## 🧠 Problem Statement
Conventional maintenance strategies rely on fixed schedules or reactive repairs after machine failure, often leading to unexpected downtime and high operational costs. This project addresses the issue by using machine learning models to predict failures before they occur, improving reliability, efficiency, and safety in manufacturing systems.

---

## 📊 Dataset
- **Dataset Name:** AI4I 2020 Predictive Maintenance Dataset  
- **Total Samples:** 10,000  
- **Dataset Type:** Synthetic but industry-realistic  
- **Target Variable:** Machine Failure (0 – No Failure, 1 – Failure)

### Features:
- Air Temperature (K)
- Process Temperature (K)
- Rotational Speed (rpm)
- Torque (Nm)
- Tool Wear (min)
- Product Type (L, M, H)

### Failure Types:
- Tool Wear Failure (TWF)
- Heat Dissipation Failure (HDF)
- Power Failure (PWF)
- Overstrain Failure (OSF)
- Random Failure (RNF)

---

## 🎯 Objectives
- Apply AI and machine learning techniques to machine assembling processes  
- Predict machine failures using sensor-based data  
- Reduce unplanned downtime and maintenance costs  
- Improve operational efficiency and machine lifespan  
- Support Industry 4.0 smart manufacturing systems  

---

## ⚙️ Methodology
1. **Data Preprocessing**
   - Data cleaning and normalization  
   - Feature scaling for distance-based learning  

2. **Model Development**
   - Implemented **K-Nearest Neighbors (KNN)** classifier  
   - Used **Random Forest** for feature importance analysis  

3. **Model Evaluation**
   - K-Fold Cross-Validation  
   - Accuracy, Precision, Recall, F1-score  
   - Specificity and ROC-AUC  

4. **Visualization**
   - Confusion Matrix  
   - ROC Curve  
   - Feature importance plots  
   - Torque distribution analysis  

---

## 🔁 Cross-Validation Strategy
K-Fold cross-validation was applied to ensure model robustness and generalization.  
For each fold, the following metrics were computed:

- Accuracy  
- Precision (Failure Class)  
- Recall (Failure Class)  
- F1-score  
- Specificity  
- ROC-AUC  

This approach ensures reliable evaluation, especially for imbalanced failure data.

---

## 🤖 Machine Learning Models Used
- **K-Nearest Neighbors (KNN)**
  - Primary predictive model
  - Effective for failure classification after feature scaling

- **Random Forest**
  - Used for feature importance and interpretability
  - Identified torque, tool wear, and rotational speed as key factors

---

## 📈 Results
- **Accuracy:** 97.7%  
- **ROC-AUC Score:** 0.89  
- **Key Influential Features:**
  - Torque  
  - Tool Wear  
  - Rotational Speed  

The model demonstrates strong performance in distinguishing between failure and non-failure conditions, making it suitable for predictive maintenance applications.

---

## 🌐 Deployment
The predictive maintenance model is deployed on **Hugging Face Spaces**, allowing users to input sensor values and receive real-time machine failure predictions.

Model Link -https://huggingface.co/spaces/Sai1012/Ai_MachineAssembly

### Deployment Features:
- Interactive input for sensor parameters  
- Instant failure prediction  
- Demonstrates real-world applicability of the model  

---

## 🏭 Applications
- Smart manufacturing systems  
- CNC machine health monitoring  
- Automotive and aerospace industries  
- Predictive maintenance platforms  
- Industry 4.0 environments  

---

## 🧪 Technologies Used
- Python  
- Scikit-learn  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Machine Learning  
- Data Visualization  

---

## 📄 Research Paper
The complete research paper is included in this repository.

**Title:** *AI in Machine Assembling*

---

## 👥 Authors
- M. Akshith Reddy  
- K. Anuroop Reddy  
- M. Kishore  
- M. Sai Venkata Karthik  
- R. Srilatha (Assistant Professor)

---

## 📚 References
- AI4I 2020 Predictive Maintenance Dataset  
- Industry 4.0 implementation frameworks  
- Machine learning and intelligent manufacturing literature  

---

## ✅ Conclusion
This project demonstrates the effectiveness of AI-driven predictive maintenance in modern manufacturing systems. By identifying machine failures in advance, industries can optimize maintenance schedules, reduce downtime, and improve overall equipment effectiveness, aligning strongly with the vision of Industry 4.0.
