from instagrapi.exceptions import (BadPassword, ChallengeRequired, ClientError,
                                   FeedbackRequired, LoginRequired,
                                   MediaNotFound, PleaseWaitFewMinutes,
                                   RateLimitError, ReloginAttemptExceeded,
                                   StoryNotFound, TwoFactorRequired,
                                   UserNotFound)

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
    PleaseWaitFewMinutes,
)
