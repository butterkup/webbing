__all__ = ("application",)


def __getattr__(name: str):
    if name == "application":
        global application
        from .main import application as A

        application = A
        return A
    raise AttributeError("Attribute %r was not found in module." % name)
