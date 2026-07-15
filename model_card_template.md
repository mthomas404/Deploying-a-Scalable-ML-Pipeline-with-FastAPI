# Model Card

## Model Details
- This model is version 1, created by Megan Thomas on July 11th, 2026.
- This model was trained on the Adult Census Income dataset using a Random Forest Classifier.
- For any questions pertaining to this model please contact me at etho813@wgu.edu. 
## Intended Use
- The intended use for this model is to predict whether an individual makes more or less than $50k a year based on various factors.
## Training Data
- The Census dataset consisted of demographic and employement related factors such as education, occupation, work class, marital status, race, sex, relationship and native country.
## Evaluation Data
- The evaluation dataset consisted of a 20% test split from the original dataset with a fixed random state (42) for reproducibility. Categorical features were processed with one hot encoding and the salary column was converted into binary format prior to training. The same prepocessing steps were used for the training and test datasets. 
## Metrics
- The metrics used were
    - Precision: 0.7466
    - Recall: 0.6359
    - F1 Score: 0.6868
## Ethical Considerations
- The dataset contains demographic information for individuals such as race, sex, marital status and native country. The outcome of models trained on this data could reinforce biases and should not be used for wage increase, lending or other decisions that could greatly impact individuals. 
## Caveats and Recommendations
- This model was trained on a single dataset and may not accurately represent other populations or recent data. The data data in the model is based off of information gathered in 1994 and could degrade the quality of data if being used for present day decision making. Future improvements could be made by performing cross validation and conducting more extensive evaluations across demographic groups. 