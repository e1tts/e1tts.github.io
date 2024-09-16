from dominate.tags import *


systems = [
    ("Prompt", "prompt"),
    ("E1 TTS (DMD)", "e1tts"),
    ("CosyVoice", "cosyvoice"),
    ("StyleTTS 2", "styletts2"),
]

ids = [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]

from eval.test_hard import test_set as samples

samples = samples[57:77]


def get_table(
    root: str = "/samples/robust",
    control_width_px=240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(
        table(cls="table table-sm")
    )
    with _div:
        with thead():
            with tr():
                th("#", scope="col")
                for spk, _, _ in samples:
                    th(str(spk), scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for key, _, _ in samples:
                        td(
                            audio(
                                source(
                                    src=f"{root}/{sys_id}/{key:03d}.wav",
                                    type="audio/wav",
                                ),
                                controls="",
                                style=f"width: {control_width_px:d}px",
                                preload="none",
                            )
                        )
    return _div
