<template>
    <div v-if="liste" class="max-w-4xl mx-auto p-6">
      <h1 class="text-2xl font-bold mb-4">🎁 {{ liste.name }}</h1>
  
      <!-- Produits -->
      <section class="mb-8">
        <h2 class="text-xl font-semibold mb-2">Produits</h2>
        <ul>
          <li v-for="produit in produits" :key="produit.id" class="flex justify-between items-center mb-2">
            {{ produit.name }} - {{ produit.price }}€
            <button @click="supprimerProduit(produit.id)" class="text-red-600">🗑️</button>
          </li>
        </ul>
  
        <form @submit.prevent="ajouterProduit" class="mt-4 flex gap-2">
          <input v-model="nouveauProduit" placeholder="Nom du produit" class="input" required />
          <input v-model.number="prixProduit" type="number" placeholder="Prix" class="input w-24" />
          <button class="btn">Ajouter</button>
        </form>
      </section>
  
      <!-- Suiveurs -->
      <section class="mb-8">
        <h2 class="text-xl font-semibold mb-2">👥 Suiveurs</h2>
        <ul>
          <li v-for="s in suiveurs" :key="s.id" class="flex justify-between items-center">
            {{ s.email }}
            <button @click="retirerSuiveur(s.id)" class="text-red-600">❌</button>
          </li>
        </ul>
      </section>
  
      <!-- Requêtes de partage -->
      <section>
        <h2 class="text-xl font-semibold mb-2">📩 Demandes d’accès</h2>
        <ul>
          <li v-for="r in requetes" :key="r.id" class="flex justify-between items-center">
            {{ r.requester.email }}
            <div class="flex gap-2">
              <button @click="accepterRequete(r.id)" class="text-green-600">✅</button>
              <button @click="refuserRequete(r.id)" class="text-red-600">❌</button>
            </div>
          </li>
        </ul>
      </section>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import api from '@/lib/axios'
  
  const route = useRoute()
  const listeId = route.params.id
  
  const liste = ref(null)
  const produits = ref([])
  const suiveurs = ref([])
  const requetes = ref([])
  
  const nouveauProduit = ref('')
  const prixProduit = ref(0)
  
  onMounted(async () => {
    await fetchListe()
  })
  
  const fetchListe = async () => {
    const res = await api.get(`api/listes/${listeId}/`)
    liste.value = res.data
    
    console.log("api/listes/${listeId}/", liste.value)

    const [prodRes, suivRes, reqRes] = await Promise.all([
      api.get(`api/produits/?liste=${listeId}`),
      api.get(`api/listes/${listeId}/followers/`),
      api.get(`api/listes/${listeId}/share-requests/`)
    ])
  
    produits.value = prodRes.data
    suiveurs.value = suivRes.data
    requetes.value = reqRes.data
  }
  
  const ajouterProduit = async () => {
    const res = await api.post('api/produits/', {
      name: nouveauProduit.value,
      price: prixProduit.value,
      liste: listeId
    })
    produits.value.push(res.data)
    nouveauProduit.value = ''
    prixProduit.value = 0
  }
  
  const supprimerProduit = async (id) => {
    await api.delete(`api/produits/${id}/`)
    produits.value = produits.value.filter(p => p.id !== id)
  }
  
  const retirerSuiveur = async (userId) => {
    await api.delete(`api/listes/${listeId}/followers/${userId}/`)
    suiveurs.value = suiveurs.value.filter(s => s.id !== userId)
  }
  
  const accepterRequete = async (id) => {
    await api.post(`api/share-requests/${id}/accept/`)
    requetes.value = requetes.value.filter(r => r.id !== id)
    await fetchListe() // pour rafraîchir les suiveurs
  }
  
  const refuserRequete = async (id) => {
    await api.post(`api/share-requests/${id}/refuse/`)
    requetes.value = requetes.value.filter(r => r.id !== id)
  }
  </script>
  
  <style scoped>
  .input {
    padding: 6px 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
  }
  
  .btn {
    background-color: #4f46e5;
    color: white;
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: bold;
  }
  </style>
  