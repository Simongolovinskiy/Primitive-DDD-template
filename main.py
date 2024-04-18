from app.infrastructure.entry_point import some_business_logic
from app.presentation.main_window import run_application


if __name__ == "__main__":
    run_application(some_business_logic)
