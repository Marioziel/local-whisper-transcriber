🎙️ Local Whisper Transcriber (CUDA Accelerated)

**Status:** 🚧 Work in Progress (WIP)

**Tech Stack:** `Python` | `Faster-Whisper` | `CUDA/NVIDIA GPU` | `CTranslate2`

A local audio transcription tool built with Python, **faster-whisper**, Whisper models, and the **CTranslate2** inference engine.

This project addresses a practical engineering need: transcribing mobile phone recordings with technical vocabulary, background noise, or distant voices using local hardware. Its goal is to improve the transcription workflow and evaluate accuracy through controlled comparisons. No project-specific accuracy improvements or performance benchmarks have been established yet.

## 🎯 Project Scope & Value

The engineering contribution is the application built around existing tools: audio file selection, transcription configuration, and output generation. Planned work includes technical vocabulary support, review aids, and systematic evaluation on representative recordings.

Whisper, faster-whisper, and CTranslate2 are developed by their respective authors and communities. This project integrates those technologies and does not train its own speech recognition model. It is an independent project with no official affiliation with OpenAI, SYSTRAN, or OpenNMT.

This repository documents a personal engineering and learning project. Development uses AI assistance, code review, and human validation of transcription results.

## 🔒 Privacy & Local Execution

Local processing is a central design goal. The current script performs inference on the computer through installed libraries and does not integrate a cloud transcription API.

Loading the model by name can still contact Hugging Face to check for or download model files. Installing dependencies also requires external repositories. **Strict offline model loading has not yet been implemented or validated.** Local inference alone does not guarantee absolute data privacy.

For recordings that must remain on the device:

- Prepare dependencies and model files before processing sensitive material.
- Run sensitive recordings outside connected AI assistants, with network access disabled when offline operation is required.
- Keep private audio, transcripts, and vocabulary files outside assistant-accessible development folders and cloud-synced locations.
- Remember that the current script prints transcript text to the terminal, where logs or screenshots may capture it.
- Publish only code, documentation, and recordings explicitly authorized for public use.

Keep `audios/`, `resultados/`, `venv/`, downloaded models, and private files out of the public repository. A `.gitignore` and a review of the files being published are pending. A `.gitignore` does not prevent file access or remove previously published data.

## ✨ Current Features

- **GPU configuration:** Uses CUDA with `float16` precision.
- **Spanish transcription:** Uses `large-v3` with the language fixed to Spanish.
- **Voice activity detection (VAD):** Filters audio based on detected speech.
- **Audio discovery:** Scans `audios/` for `.m4a`, `.mp3`, `.wav`, and `.flac` files.
- **Interactive selection:** Lets the user choose a recording when multiple files are available.
- **Named output:** Accepts a custom TXT filename or uses the audio filename.
- **Text export:** Saves UTF-8 transcripts to `resultados/` and displays segments in the terminal.
- **Windows launcher:** Includes `Transcribir.bat` for execution.

## ⚙️ How It Works

```text
[Local audio file]
        |
        v
[File selection and output name]
        |
        v
[faster-whisper: audio decoding and VAD]
        |
        v
[Whisper large-v3 through CTranslate2 on GPU/CUDA]
        |
        v
[Terminal output and local TXT export]
        |
        v
[Human review]
```

VAD settings and the use of previous transcript context will be evaluated on representative recordings. Human review follows automatic export in the current workflow.

## 📁 Planned Repository Structure

The program files will be placed at the published repository root:

```text
local-whisper-transcriber/
├── README.md
├── transcribir.py
├── Transcribir.bat
├── audios/          # Created locally; contents are excluded from publication
└── resultados/      # Created locally; contents are excluded from publication
```

The development workspace currently keeps this README in a separate `github/` folder to prepare publication. This documentation folder is not needed to run the program. The documentation draft does not include copies of the program files or imply that a GitHub repository has already been published.

## 🛠️ Requirements & Setup

The current implementation targets Windows and requires:

- Python and a virtual environment named `venv`.
- `faster-whisper` and its dependencies.
- A compatible NVIDIA GPU with CUDA/cuDNN libraries matching the installed CTranslate2 version.
- Storage for model files and enough GPU memory to load and run the model.

Automatic CPU fallback and recovery from GPU memory exhaustion are not implemented. Consult the [faster-whisper requirements](https://github.com/SYSTRAN/faster-whisper#requirements) and [CTranslate2 installation documentation](https://opennmt.net/CTranslate2/installation.html) for GPU library setup.

**Basic setup**, from the project root in a Windows terminal:

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install faster-whisper==1.2.1
New-Item -ItemType Directory -Force -Path audios, resultados
```

These commands do not install NVIDIA drivers or all required GPU libraries. Installation on a clean machine and dependency compatibility still need to be verified.

Versions identified in the development environment when preparing this README:

| Component | Version |
| --- | --- |
| Python | 3.14.6 |
| faster-whisper | 1.2.1 |
| CTranslate2 | 4.8.1 |

These are observed environment versions, not a validated compatibility matrix. A reproducible dependency file is pending.

## ▶️ Usage

1. Create `audios/` and `resultados/` if they do not exist.
2. Place an authorized test recording in `audios/`.
3. Double-click `Transcribir.bat`, or run the script from the project root:

   ```powershell
   .\venv\Scripts\python.exe transcribir.py
   ```

4. Select a recording if the program offers multiple choices.
5. Enter an output filename, or press Enter to use the audio filename.
6. Wait for processing to finish and review the TXT in `resultados/`.

Use a different output name for each experiment: the current script overwrites an existing TXT with the same name. The program's interactive messages are currently in Spanish.

## 🔧 Current Configuration

| Setting | Value | Purpose |
| --- | --- | --- |
| Model | `large-v3` | Speech recognition model |
| Language | `es` | Spanish transcription |
| Device | `cuda` | GPU execution |
| Compute type | `float16` | 16-bit floating-point computation |
| Voice filter | `vad_filter=True` | Filter audio based on speech detection |
| VAD minimum silence | `500 ms` | Silence interval used to separate speech chunks |
| Previous text context | `condition_on_previous_text=False` | Do not reuse previous output as context between windows |

These settings are the baseline for evaluation. They are not presented as optimal for every recording.

## 🚀 Roadmap

- [x] Implement audio selection and TXT export.
- [x] Integrate faster-whisper with `large-v3` and GPU configuration.
- [x] Prepare initial documentation and acknowledge upstream tools.
- [ ] Prepare code distribution with reproducible dependencies and private-file exclusions.
- [ ] Implement and validate strict offline model loading.
- [ ] Support custom technical vocabulary and recording context.
- [ ] Compare VAD settings and previous-text context options.
- [ ] Add timestamps and aids for human review.
- [ ] Measure transcription errors and processing time on authorized samples.
- [ ] Evaluate GPU memory use and feasibility of long-recording and batch workflows.
- [ ] Publish a reproducible demonstration using non-confidential data.

## 📊 Planned Evaluation

A person who has listened to the recording will prepare a corrected reference transcript. The baseline and alternative configurations will be compared on the same clips. Additional recordings will be reserved to check whether adjustments work beyond the samples used for tuning.

Evaluation will record:

- **WER (Word Error Rate):** Substitutions, deletions, and insertions divided by the number of words in the reference transcript. Lower values indicate fewer word errors.
- **Technical errors:** Mistakes in relevant terminology, numbers, and measurement units.
- **Processing time:** Recorded together with audio duration, hardware, and configuration.
- **Failure examples:** Published only when the content is authorized for disclosure.

Text normalization rules, including capitalization and punctuation handling, will be documented. Results will describe the evaluated samples, without claiming universal accuracy or perfect transcription.

## ⚠️ Known Limitations

- Names, acronyms, numbers, units, and specialized terms may be transcribed incorrectly.
- Noise, echo, overlapping voices, and unclear speech can lead to omissions, substitutions, or text unsupported by the audio.
- Current output has no timestamps or dedicated review interface.
- Speaker identification and separation of overlapping voices are not implemented.
- No project-specific accuracy metrics or systematic evaluation results have been published yet.
- Human review is required; fluent output does not guarantee a faithful transcript.

## 📚 References & Credits

Initial project references, reviewed on October 9, 2026. The bibliography will expand as features and evaluation methods are added.

1. **Radford, A., Kim, J. W., Xu, T., Brockman, G., McLeavey, C., & Sutskever, I. (2022).** *Robust Speech Recognition via Large-Scale Weak Supervision*. The research paper describing Whisper. [arXiv:2212.04356](https://arxiv.org/abs/2212.04356).
2. **OpenAI.** *Whisper*. Original speech recognition project and documentation. [Official repository](https://github.com/openai/whisper).
3. **SYSTRAN and contributors.** *faster-whisper*. The library this application uses to run Whisper models with CTranslate2. [Official repository](https://github.com/SYSTRAN/faster-whisper).
4. **OpenNMT and contributors.** *CTranslate2*. The inference engine used by faster-whisper. [Official repository](https://github.com/OpenNMT/CTranslate2) and [documentation](https://opennmt.net/CTranslate2/).

Upstream benchmarks belong to those projects and are not measurements of this application.

## 📄 License

This project's integration code is licensed under the [MIT License](LICENSE).

*Note: Whisper, faster-whisper, and CTranslate2 retain their respective open-source licenses and attribution notices. This repository does not claim ownership over these third-party AI models or inference engines.*
