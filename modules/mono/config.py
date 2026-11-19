def can_build(env, platform):
    # Kobza: the module is enabled by default, so skip it on platforms that don't support it
    # (e.g. Web) instead of aborting the build.
    if "mono" not in env.get("supported", []):
        from misc.utility.color import print_warning

        print_warning(f"The 'mono' module does not support the '{platform}' platform. Disabling it.")
        return False
    if env.get("target") == "editor" and platform not in ["windows", "macos", "linuxbsd"]:
        from misc.utility.color import print_warning

        print_warning(f"The 'mono' module does not support editor builds for the '{platform}' platform. Disabling it.")
        return False
    return True


def configure(env):
    # Check if the platform has marked mono as supported.
    supported = env.get("supported", [])
    if "mono" not in supported:
        import sys

        print("The 'mono' module does not currently support building for this platform. Aborting.")
        sys.exit(255)

    env.add_module_version_string("mono")


def get_doc_classes():
    return [
        "CSharpScript",
        "GodotSharp",
    ]


def get_doc_path():
    return "doc_classes"


def is_enabled():
    # Kobza: C# is the scripting language, so the module is enabled by default.
    # Use module_mono_enabled=no to disable it.
    return True
