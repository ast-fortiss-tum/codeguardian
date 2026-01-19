# Source: Row 19 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_287.xlsx

class TOTPStatus(IntEnum):
    DISABLED = 0
    VERIFYING = 1
    ENABLED = 2


class Member(AbstractUser):
    username_validator = printable_name

    username = CICharField(
        _("username"),
        max_length=36,
        unique=True,
        help_text=_(
            "Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists.")},
    )
    email = models.EmailField(_("email address"), blank=True, unique=True)
    state_actor = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    bio = models.TextField(blank=True, max_length=400)
    discord = models.CharField(blank=True, max_length=36)
    discordid = models.CharField(blank=True, max_length=18)
    twitter = models.CharField(blank=True, max_length=36)
    reddit = models.CharField(blank=True, max_length=36)
    team = models.ForeignKey(
        "team.Team", on_delete=SET_NULL, null=True, related_name="members"
    )
    email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=64, default=secrets.token_hex)
    password_reset_token = models.CharField(max_length=64, default=secrets.token_hex)
    points = models.IntegerField(default=0)
    leaderboard_points = models.IntegerField(default=0)
    last_score = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    def can_login(self):
        return (
            self.is_staff
            or config.get("enable_prelogin")
            or (config.get("enable_login") and config.get("start_time") <= time.time())
        )

    def issue_token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token.key

    def has_2fa(self):
        return self.totp_device is not None and self.totp_device.verified