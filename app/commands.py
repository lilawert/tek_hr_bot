from aiogram.types import BotCommand
from locales.loader import t
COMMANDS = [
    BotCommand(command="start", description=t("service.commands.start")),
]

USER_COMMANDS = COMMANDS + [
    BotCommand(command="help", description=t("service.commands.help")),
    BotCommand(command="company", description=t("service.commands.company")),
    BotCommand(command="im", description=t("service.commands.im")),
    BotCommand(command="vtours", description=t("service.commands.vtours")),
    BotCommand(command="structure", description=t("service.commands.structure")),
    BotCommand(command="cafeteria", description=t("service.commands.cafeteria")),
    BotCommand(command="schedule", description=t("service.commands.schedule")),
    BotCommand(command="support", description=t("service.commands.support")),
    BotCommand(command="docs", description=t("service.commands.docs")),
]

ADMIN_COMMANDS = USER_COMMANDS + [
    BotCommand(command="pincode", description=t("service.commands.link")),
    BotCommand(command="content", description=t("service.commands.content")),
]