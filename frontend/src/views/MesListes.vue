<template>
    <div class="p-6">
      <h1 class="text-2xl font-bold mb-4">Mes Wish Lists</h1>
  

      <div v-if="errorMsg" class="error-banner">
        {{ errorMsg }}
      </div>
      <button @click="openNewModal" class="bg-green-600 text-white px-4 py-2 rounded mb-4">
        ➕ Nouvelle liste
      </button>
  
      <div v-if="listes.length === 0">
        <p>Aucune liste pour le moment. Crée ta première !</p>
      </div>
  
      <ul class="space-y-4">
        <li v-for="liste in listes" :key="liste.id" class="p-4 border rounded-lg shadow">
          <div class="flex justify-between items-center">
            <div>
              <h2 class="text-xl font-semibold">{{ liste.name }}</h2>
              <p class="text-sm text-gray-500">Partagée : {{ liste.is_shared ? 'Oui' : 'Non' }}</p>
            </div>
  
            <div class="flex space-x-2">
              <button @click="editListe(liste)" class="text-blue-600 hover:underline">✏️ Modifier</button>
              <button @click="deleteListe(liste.id)" class="text-red-600 hover:underline">🗑️ Supprimer</button>
              <button @click="copyShareLink(liste)" class="text-gray-700 hover:underline">📋 Copier le lien</button>
            </div>
          </div>
        </li>
      </ul>
  
      <!-- Modal de création/modification -->
      <div v-if="showModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
        <div class="bg-white p-6 rounded-lg w-full max-w-md">
          <h2 class="text-xl font-bold mb-4">{{ editingListe ? 'Modifier la liste' : 'Nouvelle liste' }}</h2>
          <input v-model="form.name" placeholder="Nom de la liste" class="border w-full p-2 rounded mb-3" />
  
          <label class="block mb-2">
            <input type="checkbox" v-model="form.is_shared" />
            Liste partagée
          </label>
  
          <div class="flex justify-end space-x-2 mt-4">
            <button @click="closeModal" class="text-gray-600">Annuler</button>
            <button @click="submitForm" class="bg-blue-600 text-white px-4 py-2 rounded">
              {{ editingListe ? 'Enregistrer' : 'Créer' }}
            </button>
          </div>
        </div>
      </div>
    </div>
</template>
  
<script setup>
  import { ref, onMounted } from 'vue'
  import instance from '@/lib/axios';
  
  const listes = ref([])
  const showModal = ref(false)
  const editingListe = ref(null)
  const errorMsg = ref('')
  
  const form = ref({
    name: '',
    is_shared: false
  })
  
  const fetchListes = async () => {
    try {
      const res = await instance.get('/api/listes/')
      if (res.status === 200 && Array.isArray(res.data)) {
        listes.value = res.data
      } else {
        console.warn("Réponse inattendue :", res)
        errorMsg.value = "Impossible de charger vos listes. Veuillez réessayer plus tard."
      }
    } catch (error) {
      console.error("Erreur lors du chargement des listes :", error)
      // Tu pourrais afficher un message à l'utilisateur ici si tu veux
      errorMsg.value = "Impossible de charger vos listes. Veuillez réessayer plus tard."
    }
  }

  
  const openNewModal = () => {
    editingListe.value = null
    form.value = { name: '', is_shared: false }
    showModal.value = true
  }
  
  const editListe = (liste) => {
    editingListe.value = liste
    form.value = { name: liste.name, is_shared: liste.is_shared }
    showModal.value = true
  }
  
  const closeModal = () => {
    showModal.value = false
  }
  
  const submitForm = async () => {
    if (editingListe.value) {
      await instance.put(`/api/listes/${editingListe.value.id}/`, form.value)
    } else {
      await instance.post('/api/listes/', form.value)
    }
    await fetchListes()
    closeModal()
  }
  
  const deleteListe = async (id) => {
    if (confirm('Supprimer cette liste ?')) {
      await instance.delete(`/api/listes/${id}/`)
      await fetchListes()
    }
  }
  
  const copyShareLink = (liste) => {
    const link = `${window.location.origin}/listes/join/${liste.share_token}/`
    navigator.clipboard.writeText(link)
    alert('Lien copié dans le presse-papiers !')
  }
  
  onMounted(fetchListes)
</script>
  
<style scoped>
  button:hover {
    cursor: pointer;
  }

  .error-banner {
    background-color: #fee2e2;  /* rouge très pâle */
    color: #b91c1c;             /* rouge foncé pour le texte */
    padding: 12px 16px;
    border-radius: 6px;
    border: 1px solid #fca5a5;
    margin-bottom: 16px;
    font-size: 0.95rem;
  }

</style>
  