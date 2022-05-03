import pandas as pd


def clean_data(df):
    df.loc[df['Label'] == "moisturizing-cream-oils-mists", 'Label'] = "moisturizer"
    df.loc[df['Label'] == "facial-treatments", 'Label'] = "face_treatment"
    df.loc[df['Label'] == "face-mask", 'Label'] = "face_mask"
    df.loc[df['Label'] == "eye-treatment-dark-circle-treatment", 'Label'] = "eye_treatment"
    df.loc[df['Label'] == "sunscreen-sun-protection", 'Label'] = "sunscreen"
    df.drop(columns=['URL'], inplace=True)


if __name__ == '__main__':
    df = pd.read_csv('data/cosmetic.csv')
    clean_data(df)
