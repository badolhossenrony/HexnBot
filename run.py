from cosmos import get_bot

if __name__ == "__main__":
    bot = get_bot(NzE1MTI5NjAyODEyNDExOTQ1.Xun1-g._MSwzvq60uEwsMccdeKUfRzvmsg)
    try:
        bot.eh.sentry.init(**bot.configs.sentry.raw)  # Initialise sentry for deeper integration.
    except bot.eh.sentry.utils.BadDsn:
        bot.log.error("Invalid sentry DSN provided.")
    bot.log.info(f"All initial tasks completed. [{bot.time.round_time()} seconds.]")
    bot.run()
