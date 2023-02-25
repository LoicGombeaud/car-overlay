<script>
import { saveAs } from "file-saver"

const backUrl = "https://pdv-auto.loicgombeaud.com"

export default {
  data() {
    return {
      file: null,
      showResult: false
    }
  },
  methods: {
    onChange(event) {
      this.file = event.target.files[0]
    },
    async onSubmit() {
      //TODO better input validation?
      if (!this.file) {
        return
      }

      var submitButton = this.$refs.submit

      this.showResult = false
      submitButton.disabled = true
      submitButton.innerHTML = "2. Traitement en cours..."

      var formData = new FormData()
      formData.append("file", this.file)
      var res = await fetch(`${backUrl}/upload`, { method: "POST", body: formData })
      var blob = await res.blob()
      var filenameTrimmed = this.file.name.replace(/\.[^/.]+$/, "")
      saveAs(blob, `${filenameTrimmed}-overlay.mp4`)

      this.showResult = true
      submitButton.disabled = false
      submitButton.innerHTML = "2. Lancement du traitement"
    },
  },
}
</script>

<template>
  <form novalidate @submit.prevent="onSubmit">
    <div class="my-5">
      <label for="formFileLg" class="form-label">1. Upload de la vidéo (.mp4 uniquement, 50 Mo maximum)</label>
      <input
        class="form-control form-control-lg"
        id="formFileLg"
        type="file"
        accept=".mp4"
        @change="onChange"
        >
    </div>
    <div class="my-5">
        <button type="submit" ref="submit" class="btn btn-primary mb-3">2. Lancement du traitement</button>
    </div>
  </form>
  <p v-if="showResult">3. Traitement terminé ! Téléchargement en cours</p>
</template>
