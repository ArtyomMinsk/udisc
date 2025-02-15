from datetime import datetime
import pandas as pd

def read_udisc_data() -> pd.DataFrame:
    df = pd.read_csv("data/scorecards.csv")
    return df


def main() -> None:
    df = read_udisc_data()
    print(df.head())

def test_read_udisc_data():
    # Test that the function returns a pandas DataFrame
    df = read_udisc_data()
    assert isinstance(df, pd.DataFrame)
    
    # Test that the DataFrame is not empty
    assert not df.empty
    
    # Test that the DataFrame has the expected columns
    expected_columns = ['Date', 'Course', 'Layout', 'Total']  # Add actual column names
    for col in expected_columns:
        assert col in df.columns

if __name__ == "__main__":
    main()