import enum

from commitizen import out


class ExitCode(enum.IntEnum):
    EXPECTED_EXIT = 0
    NO_COMMITIZEN_FOUND = 1
    NOT_A_GIT_PROJECT = 2
    NO_COMMITS_FOUND = 3
    NO_VERSION_SPECIFIED = 4
    NO_PATTERN_MAP = 5
    COMMIT_FAILED = 6
    TAG_FAILED = 7
    NO_ANSWERS = 8
    COMMIT_ERROR = 9
    NO_COMMIT_BACKUP = 10
    NOTHING_TO_COMMIT = 11
    CUSTOM_ERROR = 12
    NO_COMMAND_FOUND = 13
    INVALID_COMMIT_MSG = 14
    MISSING_CONFIG = 15
    NO_REVISION = 16
    CURRENT_VERSION_NOT_FOUND = 17
    INVALID_COMMAND_ARGUMENT = 18


class CommitizenException(Exception):
    def __init__(self, *args, **kwargs):
        self.output_method = kwargs.get("output_method") or out.error
        self.exit_code = self.__class__.exit_code
        if args:
            self.message = args[0]
        elif hasattr(self.__class__, "message"):
            self.message = self.__class__.message
        else:
            self.message = ""

    def __str__(self):
        return self.message


class ExpectedExit(CommitizenException):
    exit_code = ExitCode.EXPECTED_EXIT


class DryRunExit(ExpectedExit):
    pass


class NoCommitizenFoundException(CommitizenException):
    exit_code = ExitCode.NO_COMMITIZEN_FOUND


class NotAGitProjectError(CommitizenException):
    exit_code = ExitCode.NOT_A_GIT_PROJECT
    message = "fatal: not a git repository (or any of the parent directories): .git"


class MissingConfigError(CommitizenException):
    exit_code = ExitCode.MISSING_CONFIG
    message = "fatal: customize is not set in configuration file."


class NoCommitsFoundError(CommitizenException):
    exit_code = ExitCode.NO_COMMITS_FOUND


class NoVersionSpecifiedError(CommitizenException):
    exit_code = ExitCode.NO_VERSION_SPECIFIED


class NoPatternMapError(CommitizenException):
    exit_code = ExitCode.NO_PATTERN_MAP


class CommitFailedError(CommitizenException):
    exit_code = ExitCode.COMMIT_FAILED


class TagFailedError(CommitizenException):
    exit_code = ExitCode.TAG_FAILED


class CurrentVersionNotFoundError(CommitizenException):
    exit_code = ExitCode.CURRENT_VERSION_NOT_FOUND


class NoAnswersError(CommitizenException):
    exit_code = ExitCode.NO_ANSWERS


class CommitError(CommitizenException):
    exit_code = ExitCode.COMMIT_ERROR


class NoCommitBackupError(CommitizenException):
    exit_code = ExitCode.NO_COMMIT_BACKUP


class NothingToCommitError(CommitizenException):
    exit_code = ExitCode.NOTHING_TO_COMMIT


class CustomError(CommitizenException):
    exit_code = ExitCode.CUSTOM_ERROR


class InvalidCommitMessageError(CommitizenException):
    exit_code = ExitCode.INVALID_COMMIT_MSG


class NoRevisionError(CommitizenException):
    exit_code = ExitCode.NO_REVISION


class NoCommandFoundError(CommitizenException):
    exit_code = ExitCode.NO_COMMAND_FOUND


class InvalidCommandArgumentError(CommitizenException):
    exit_code = ExitCode.INVALID_COMMAND_ARGUMENT
