import os
import sentry_sdk

from validator import validate_phone

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
)


def main():
    phone = input("Введіть номер: ")

    try:
        if validate_phone(phone):
            print("Номер правильний ✅")
        else:
            print("Номер неправильний ❌")
    except ValueError as e:
        sentry_sdk.capture_exception(e)
        print("Помилка:", e)


if __name__ == "__main__":
    main()
