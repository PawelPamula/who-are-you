#!/usr/bin/env python
import os
import sys

from webfest.base.factory import create_app

from flask_collect import Collect
from flask_script import Manager, Server, Shell, prompt_choices
from flask_script.commands import ShowUrls, Clean
from flask_assets import ManageAssets

env = os.environ.get('webfest_ENV', 'dev')
instance_path = ""
if env == "Heroku":
    instance_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "webfest", "base", "instance"
    )

app = create_app(instance_path=instance_path, env=env)

manager = Manager(app=app)
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())
manager.add_command("shell", Shell())
manager.add_command("assets", ManageAssets())

collect = Collect()
collect.init_app(app)
collect.init_script(manager)

if __name__ == "__main__":
    manager.run()
