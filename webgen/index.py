import dominate
from dominate.tags import *
from dominate.util import raw


doc = dominate.document(title=None)

with doc.head:
    meta(charset="utf-8")
    meta(http_equiv="X-UA-Compatible", content="IE=edge")
    meta(name="viewport", content="width=device-width, initial-scale=1")
    title("E1 TTS Online Supplement")
    link(href="/statics/bootstrap-5.2.3-dist/css/bootstrap.min.css", rel="stylesheet")
    link(href="/statics/my.css", rel="stylesheet")

with doc:
    # Title and Metadata:
    with div(cls="container").add(div(cls="row")):
        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            # Header
            h2(
                """E1 TTS: Simple and Fast Non-Autoregressive TTS""",
                style="text-align: center",
            )
            with div(cls="row justify-content-md-center"):
                with div(cls="col-md-auto"):
                    em(
                        p(
                            span("Zhijun Liu", sup("1"), cls="me-3"),
                            span("Shuai Wang", sup("2,1"), cls="me-3"),
                            span("Pengcheng Zhu", sup("3"), cls="me-3"),
                            span("Mengxiao Bi", sup("3"), cls="me-3"),
                            span("Haizhou Li", sup("1,2")),
                            cls="text-center, mb-1",
                        )
                    )
                with div(cls="col-md-10"):
                    with div(cls="text-center"):
                        p(
                            span("School of Data Science", sup("1"), cls="me-3"),
                            span(
                                "Shenzhen Research Institute of Big Data",
                                sup("2"),
                            ),
                            cls="mb-0",
                        )
                        p(
                            "The Chinese University of Hong Kong, Shenzhen",
                            cls="mb-0",
                        )
                        p(
                            "Fuxi AI Lab, NetEase Inc.",
                            sup("3"),
                            cls="mb-0",
                        )
            br()
            img(
                src="/statics/main.svg",
                alt="Overview of E1 TTS model.",
                cls="img-fluid mx-auto d-block",
                style="width: 100%; max-width: 800px;",
            )
            br()
            h3("Abstract")
            p(
                raw(
                    """This paper introduces Easy One-Step Text-to-Speech (E1 TTS), an efficient non-autoregressive zero-shot text-to-speech """
                    """system based on denoising diffusion pretraining and distribution matching distillation. The training of E1 TTS is """
                    """straightforward; it does not require explicit monotonic alignment between the text and audio pairs. """
                    """The inference of E1 TTS is efficient, requiring only one neural network evaluation for each utterance. """
                    """Despite its sampling efficiency, E1 TTS achieves naturalness and speaker similarity comparable to various strong baseline models."""
                ),
                _class="lead",
            )
            p(
                "This ",
                a(
                    "github repository",
                    href="https://github.com/e1tts/e1tts.github.io/",
                ),
                " contains the audio samples, and the evaluation code and file lists.",
                cls="lead",
            )

            # Prompt Generation:
            from .prompt import get_table as get_table_prompt

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            h3("Prompted Generation")
            p(
                "TTS models generate target speech, given 3 seconds prompt speech as reference.",
                cls="lead",
            )
            get_table_prompt()

        from .inpaint import get_table as get_table_inpaint

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            h3("Speech Inpainting")
            p(
                "TTS models try to recover masked speech, given unmasked speech and the complete text as reference. Here we mask the middle one third (about 2 seconds long) for benchmarking.",
                cls="lead",
            )
            get_table_inpaint()

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from .robust import get_table as get_table_demo_robust

            h3("Prompted Generation on Hard Samples")
            p(
                """Prompted generation again, but with hard text inputs proposed in ELLA-V.""",
                cls="lead",
            )
            get_table_demo_robust()

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from .celeb import get_table as get_table_celeb

            h3("Extra Samples: Voice Cloning Celebrities")
            p(
                "E1 TTS trained only on LibriTTS is capable of imitating famous figures' voice. Prompts and baseline results are obtained from demo pages of CLaM-TTS and DiTTo-TTS. "
                "For E1 TTS results in this section, we picked the best result in 3 generations.",
                cls="lead",
            )
            get_table_celeb()

        with div(cls="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded"):
            from .demo_compare import get_table as get_table_demo_compare

            h3("Extra Samples: Compare with Proprietary Systems on Prompted Generation")
            p(
                """In this section, we compare our system with proprietary systems (as of 16 Sep 2024) on prompted generation. """
                """The following samples are obtained from their online demo pages. All waveforms are downsampled to 16kHz. """
                """The audios in this section may sound bad due to the 16kHz sampling rate and noisy speech prompts.""",
                cls="lead",
            )
            get_table_demo_compare()

with doc.footer:
    script(src="/statics/jquery/jquery-3.7.1.slim.min.js")
    script(src="/statics/bootstrap-5.2.3-dist/bootstrap.min.js")

# Script for allowing only one audio to play at the same time:
doc.children.append(
    script(
        raw(
            """
            $(function(){
                $("audio").on("play", function() {
                    $("audio").not(this).each(function(index, audio) {
                        audio.pause();
                        audio.currentTime = 0;
                    });
                });
            });
            """
        )
    )
)

with open("index.html", "w") as index:
    index.write(doc.render())
