ANNOTATOR_ID = 'annotator_id'
TELEMETRY_URL = 'https://telemetry.anish.io/api/v1/submit'
TELEMETRY_DELTA = 20 * 60 # seconds
SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"

# Setting
# keys
SETTING_CLOSED = 'closed' # boolean
SETTING_TELEMETRY_LAST_SENT = 'telemetry_sent_time' # integer
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
# these can be overridden via the config file
DEFAULT_WELCOME_MESSAGE = '''
Welcome to our Highline Freestyle Trick difficulty evaluation.

**Please read this important message carefully before continuing.**

The system is based on the model of pairwise comparison. You'll start off by
looking at a single trick, and then for every other trick after that,
you'll decide whether it's harder or easier than the one you looked at
**beforehand**.

If at any point, you can't tell the difficulty of a particular trick, you can click the
'Skip' button. **Please rate only trick you can do! Don't try to guess!**

This is an effort to try ranking all tricks in an order, which could be used for judging
future competitions. **Once you make a decision, you can't take it back**.
'''.strip()

DEFAULT_EMAIL_SUBJECT = 'Welcome to Gavel!'

DEFAULT_EMAIL_BODY = '''
Hi {name},

Welcome to Gavel, the online expo judging system. This email contains your
magic link to the judging system.

DO NOT SHARE this email with others, as it contains your personal magic link.

To access the system, visit {link}.

Once you're in, please take the time to read the welcome message and
instructions before continuing.
'''.strip()

DEFAULT_CLOSED_MESSAGE = '''
The system is currently closed. Reload the page to try again.
'''.strip()

DEFAULT_DISABLED_MESSAGE = '''
Your account is currently disabled. Reload the page to try again.
'''.strip()

DEFAULT_LOGGED_OUT_MESSAGE = '''
You are currently logged out. Open your magic link to get started.
'''.strip()

DEFAULT_WAIT_MESSAGE = '''
That's all for now.

You can come back if someone stuck some new tricks and also rank these ones.
'''.strip()
