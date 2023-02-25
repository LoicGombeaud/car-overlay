<script>
const backUrl = "http://localhost:8080"
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
    onSubmit() {
      //TODO better input validation
      if (!this.file) {
        return
      }
      var submitButton = this.$refs.submit
      submitButton.disabled = true
      submitButton.innerHTML = "2. Traitement en cours..."

      var formData = new FormData()
      formData.append("video", this.file)
      console.log(formData)
      fetch(`${backUrl}/upload`, { method: "POST", body: formData })
    },
  },
}
</script>

<template>
  <form novalidate @submit.prevent="onSubmit">
    <div class="my-5">
      <label for="formFileLg" class="form-label">1. Upload de la vidéo</label>
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
  <p v-if="showResult">3. Traitement terminé, téléchargement en cours</p>
</template>
