# Kobza

## 2D and 3D cross-platform game engine

**Kobza is a feature-packed, cross-platform game engine to create 2D and 3D
games from a unified interface.** Games can be exported to the major desktop
platforms (Linux, macOS, Windows), mobile platforms (Android, iOS), as well as
Web-based platforms.

## Free and open source

Kobza is completely free and open source under the [MIT license](LICENSE.txt).
No strings attached, no royalties, nothing. The users' games are theirs, down
to the last line of engine code.

## Origins

Kobza is an independent fork of [Godot Engine](https://github.com/godotengine/godot),
created in 2026 from its `master` branch (4.8 development cycle). Kobza is not
affiliated with or endorsed by the Godot Engine project or the Godot Foundation.

The original code remains under its original copyright, see
[LICENSE.txt](LICENSE.txt), [COPYRIGHT.txt](COPYRIGHT.txt) and
[AUTHORS.md](AUTHORS.md) for details.

## Getting the engine

### Compiling from source

Kobza uses the [SCons](https://scons.org/) build system. A minimal build of the
editor on Linux looks like this:

```bash
scons platform=linuxbsd target=editor
```

The resulting binary is placed in the `bin/` folder. Run `scons --help` for the
list of build options.

## Contributing

To get started contributing to the project, see the [contributing guide](CONTRIBUTING.md).
This document also includes guidelines for reporting bugs.

Bug reports and feature requests go to the
[issue tracker](https://github.com/RSapeliuk/kobza/issues).
