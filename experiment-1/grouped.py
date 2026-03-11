import pandas as pd

try:
    # Input number of class intervals
    num_classes = int(input("Enter the number of class intervals: "))

    classes_data = []

    print("\nEnter details for each class (lowerLimit upperLimit frequency)")
    for i in range(num_classes):
        line = input(f"Class {i+1} (eg: 10 20 5): ").split()
        l, u, f = map(float, line)
        classes_data.append({
            "lowerlimit": l,
            "upperlimit": u,
            "frequency": f
        })

    df = pd.DataFrame(classes_data)

    df["Midpoint"] = (df["lowerlimit"] + df["upperlimit"]) / 2
    df["cumulative_frequency"] = df["frequency"].cumsum()

    n = df["frequency"].sum()
    h = df["upperlimit"].iloc[0] - df["lowerlimit"].iloc[0]

    mean = (df["Midpoint"] * df["frequency"]).sum() / n

    median_class_index = df[df["cumulative_frequency"] >= n / 2].index[0]
    median_class = df.iloc[median_class_index]

    l_med = median_class["lowerlimit"]
    f_med = median_class["frequency"]
    prev_cf = df["cumulative_frequency"].iloc[median_class_index - 1] if median_class_index > 0 else 0

    median = l_med + (((n / 2) - prev_cf) / f_med) * h

    modal_class_index = df["frequency"].idxmax()
    modal_class = df.iloc[modal_class_index]

    l_mod = modal_class["lowerlimit"]
    f1 = modal_class["frequency"]
    f0 = df["frequency"].iloc[modal_class_index - 1] if modal_class_index > 0 else 0
    f2 = df["frequency"].iloc[modal_class_index + 1] if modal_class_index < len(df) - 1 else 0

    denominator = (2 * f1 - f0 - f2)
    mode = l_mod + ((f1 - f0) / denominator) * h if denominator != 0 else l_mod

    print("Mean  :", mean)
    print("Median:", median)
    print("Mode  :", mode)

except Exception as e:
    print("Unexpected error:", e)
