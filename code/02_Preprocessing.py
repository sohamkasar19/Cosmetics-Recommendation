import pandas as pd


def clean_data(df):
    df.loc[df['Label'] == "moisturizing-cream-oils-mists", 'Label'] = "moisturizer"
    df.loc[df['Label'] == "facial-treatments", 'Label'] = "face_treatment"
    df.loc[df['Label'] == "face-mask", 'Label'] = "face_mask"
    df.loc[df['Label'] == "eye-treatment-dark-circle-treatment", 'Label'] = "eye_treatment"
    df.loc[df['Label'] == "sunscreen-sun-protection", 'Label'] = "sunscreen"
    df.drop(columns=['URL'], inplace=True)


def preprocess_ingredients(df):
    df.dropna(subset=['ingredients'], inplace=True)
    processed_ingredient = [t.split('\n') for t in df['ingredients']]
    pattern = ['\r\n', 'Please', 'No Info', 'This product', 'Visit']

    for i in range(len(df)):
        num = len(processed_ingredient[i])
        for j in range(num):
            if all(x not in processed_ingredient[i][j] for x in pattern):
                df['ingredients'][i] = processed_ingredient[i][j]
    return df


if __name__ == '__main__':
    df = pd.read_csv('data/cosmetic.csv', na_values={'NA', '#NAME?'})
    clean_data(df)
    df = preprocess_ingredients(df)
