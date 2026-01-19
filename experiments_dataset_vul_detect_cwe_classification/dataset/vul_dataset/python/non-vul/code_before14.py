# Source: Row 740 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def get(self):
    if not current_user.is_authenticated:
        return "Must be logged in to log out", 200

    logout_user()
    return "Logged Out", 200