import sentry_sdk


def init_sentry():
    sentry_sdk.init(
        dsn="https://f9828f61bf90991d8890184e11b81b14@o4511343270035456.ingest.de.sentry.io/4511343278751824",  # noqa: E501
        # Add data like request headers and IP for users,
        # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
        send_default_pii=True,
    )


def check_latency(number):
    if not isinstance(number, int):
        raise ValueError("Entered value is not a number")
    if (number < 100):
        raise ValueError("Entered numer is smaller that 100")
    else:
        return "Your number is correct"


def main():
    init_sentry()
    try:
        user_input = int(input("Enter number:"))
        result = check_latency(user_input)
        print(result)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        raise


if __name__ == "__main__":
    main()
