Entry Points Demo
=================
This repo shows how you can use entry points to create a pluggable interface for your
distribution.

Installation
------------
#. **Activate the virtualenv for the py-ttw-day-3 repo.**
#. Install this project by running the following command::

      pip install .

   .. note::

      Use ``pip`` instead of ``pipenv`` to avoid adding this distro to your project's
      ``Pipfile`` and ``Pipfile.lock``.

#. Switch back to the ``py-ttw-day-3`` directory.
#. Run the following command::

      git checkout entry-points-demo

#. Lastly, run the following command to verify that it worked::

      pipenv run app-cli --help

You should see output that looks like this::

   > pipenv run app-cli --help
   Loading .env environment variables...

    Usage: python -m cli.main [OPTIONS] COMMAND [ARGS]...

   ╭─ Options ────────────────────────────────╮
   │ --help     Show this message and exit.   │
   ╰──────────────────────────────────────────╯
   ╭─ Commands ─╮
   │ extras     │
   │ generate   │
   │ profiles   │
   ╰────────────╯

Note the presence of the ``extras`` command, loaded into your app using entry points.

How does it work?
=================
In the app
----------
In the ``py-ttw-day-3`` codebase, with the ``entry-points-demo`` branch checked out, you
can find some additional code in ``src/cli/main.py``:

.. code-block:: py

   # Register additional commands from plugins.
   for e in entry_points(group="app.command"):
       plugin: typer.Typer = e.load()

       if not isinstance(plugin, typer.Typer):
           raise TypeError(
               f"Invalid plugin {e.name} ({type(plugin).__name__}); typer.Typer expected"
           )

       app.add_typer(plugin, name=e.name)

This code looks for packages that have registered entry points using the group name
"app.command".  For each one that it finds, it loads the corresponding object and adds
it to the Typer interface via ``app.add_typer()``.

In the plugin (this repo)
-------------------------
Meanwhile, in this project's `pyproject.toml <./pyproject.toml>`, you can find this
configuration:

.. code-block:: toml

   [project.entry-points."app.command"]
   extras = "entry_points_demo.commands.extras:command"

When you ``pip install`` this project into your ``py-ttw-day-3`` virtualenv, this also
includes the entry points configuration, so that the app can find them when it runs.
