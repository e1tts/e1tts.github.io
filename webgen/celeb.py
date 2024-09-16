from dominate.tags import *
from dominate.util import raw
from pathlib import Path

systems = [
    ("Prompt", "prompt"),
    ("E1 TTS", "e1tts"),
    ("DiTTo-TTS", "ditto"),
    ("ARDiT (DMD, B=1)", "ardit_dmd_b1"),
    ("CLaM-TTS", "clamtts"),
]

samples = [
    (
        "caine",
        "Michael Caine",
        "What you need to be a star in movies is not that different from what you need to be a star in the other universe. It just takes a little more luck.",
        "And sometimes, in both realms, it's not just about shining the brightest, but enduring the longest.",
    ),
    (
        "jessie",
        "Jessie Eisenberg",
        "I'm starting this, twelve minutes late which is annoying and not my fault. Rachel needed my help and Ziggy would not stop crying.",
        "So here we are, trying to catch up, and hoping this day turns around soon.",
    ),
    (
        "optimusprime",
        "Optimus Prime",
        "Perhaps, in any case, we had better see some improvement, or this battle may be lost before it has truly begun.",
        "We must unite and harness our strengths, for the fate of our world hangs in the balance.",
    ),
    (
        "rachel",
        "Rachel McAdams",
        "So far, the ordinary observer, an extraordinary observer might have seen that the chin was very pointed and pronounced.",
        "But to those who knew her well, it was a symbol of her unwavering determination and spirit.",
    ),
    (
        "robert",
        "Robert Downey Jr.",
        "They, say the best weapon is one you never have to fire. I respectfully disagree! I prefer, the weapon you only have to fire once! That's how dad did it! that's how America does it! and it's worked out pretty well so far.",
        "We have the responsibility to ensure power and technology are used for the greater good.",
    ),
    (
        "sherlock",
        "Benedict Cumberbatch",
        "So maybe, that you would prefer to forgo my secret rather than consent to becoming a prisoner here for what might be several days.",
        "However, if you choose to stay, know that the truth I unveil may forever alter the course of your journey.",
    ),
    (
        "zuck",
        "Mark Zuckerberg",
        "Alright so our team developed the first speech to speech AI translation system, that works for languages that are only spoken and not written like Hokkien.",
        "Our goal is to bridge communication gaps and preserve the richness of these unique languages.",
    ),
]

cartoon = [
    (
        "dwarf",
        "Dwarf from Warcraft",
        "May the mountain gods guide you.",
        "Good afternoon everyone. Today, we are super excited to introduce you all to Introduction to Deep Learning, the course of Carnegie Mellon University.",
    ),
    (
        "obama",
        "Barack Obama",
        "Eleven workers lost their lives. Seventeen others were injured. And soon, nearly a mile beneath the surface of the ocean, oil began spewing into the water.",
        "Good afternoon everyone. Today, we are super excited to introduce you all to Introduction to Deep Learning, the course of Carnegie Mellon University.",
    ),
    (
        "may",
        "Theresa May",
        "The New Year is a time to reflect on what has passed, and to look ahead to the opportunities to come. And this year, as I consider all that twenty seventeen has in store, I believe those opportunities are greater than ever.",
        "Good afternoon everyone. Today, we are super excited to introduce you all to Introduction to Deep Learning, the course of Carnegie Mellon University.",
    ),
    (
        "spongebob",
        "Sponge Bob",
        "My name is Spongebob Squarepants. And I’m gonna tell you about paying.",
        "Let's go drink until we can't feel feelings anymore.",
    ),
    (
        "petergriffin",
        "Peter Griffin",
        "Well, I, I’m getting something really special too and by special, I don’t mean special like that Kleinman boy down the street. More special, like, like special K the serial.",
        "Uh, it's not like the internet to go crazy about something small and stupid.",
    ),
    (
        "rick",
        "Rick Sanchez",
        "Yeah, that’s the difference between you and me morty. I never go back to the carpet store.",
        "Then I would never talk to that person about boa constrictors, or primeval forests, or stars. I would bring myself down to his level.",
    ),
    (
        "morty",
        "Morty Smith",
        "Yeah, that’s the difference between you and me morty. I never go back to the carpet store.",
        "Then I would never talk to that person about boa constrictors, or primeval forests, or stars. I would bring myself down to his level.",
    ),
]


def get_table(
    root: str = "/samples/celeb",
    control_width_px=240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(
        table(cls="table table-sm")
    )
    with _div:
        with thead():
            with tr():
                th("#", scope="col")
                for _, name, _, _ in samples:
                    th(name, scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for nick, _, _, _ in samples:
                        wav_path = Path(f"{root[1:]}/{sys_id}/{nick}.wav")
                        if wav_path.exists():
                            td(
                                audio(
                                    source(
                                        src=f"{root}/{sys_id}/{nick}.wav",
                                        type="audio/wav",
                                    ),
                                    controls="",
                                    style=f"width: {control_width_px:d}px",
                                    preload="none",
                                )
                            )
                        else:
                            td("—", cls="center-text")
    return _div
