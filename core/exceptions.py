from instagrapi.exceptions import (
    LoginRequired,
    ClientError,
    UserNotFound,
    MediaNotFound,
    StoryNotFound,
    RateLimitError,
    ChallengeRequired,
    TwoFactorRequired,
    FeedbackRequired,
    ReloginAttemptExceeded,
    BadPassword,
    PleaseWaitFewMinutes
)

ALL_EXCEPTIONS = (
    LoginRequired,
    ClientError,
    UserNotFound,
    MediaNotFound,
    StoryNotFound,
    RateLimitError,
    ChallengeRequired,
    TwoFactorRequired,
    FeedbackRequired,
    ReloginAttemptExceeded,
    BadPassword,
    PleaseWaitFewMinutes
)