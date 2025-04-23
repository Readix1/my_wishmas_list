<template>
    <div class="max-w-md mx-auto mt-12 p-6 border rounded shadow">
      <h2 class="text-2xl font-bold mb-6">🔐 Connexion</h2>
  
      <div v-if="errorMsg" class="error-banner">
        {{ errorMsg }}
      </div>
  
      <form @submit.prevent="handleLogin">
        <label class="block mb-2">Email</label>
        <input v-model="email" type="email" required class="input" />
  
        <label class="block mt-4 mb-2">Mot de passe</label>
        <input v-model="password" type="password" required class="input" />
  
        <button type="submit" class="btn mt-6 w-full">Se connecter</button>
      </form>
    </div>
  </template>
  
  <script setup>
import { ref } from 'vue'
import instance from '@/lib/axios' // ton instance Axios personnalisée

const email = ref('')
const password = ref('')
const errorMsg = ref('')

const handleLogin = async () => {
  try {
    const res = await instance.post('api/token/', {
      username: email.value,
      password: password.value
    })

    const token = res.data.token
    localStorage.setItem('authToken', token)

    // Ajoute le token à axios pour les futures requêtes
    instance.defaults.headers.common['Authorization'] = `Token ${token}`

    // Redirige vers la page principale
    window.location.href = '/listes'
  } catch (err) {
    errorMsg.value = 'Identifiants invalides ou serveur injoignable.'
    console.error('Erreur de connexion :', err)
  }
}
  </script>
  
  <style scoped>
  .input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
  }
  
  .btn {
    background-color: #4f46e5;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 6px;
    font-weight: bold;
  }
  
  .error-banner {
    background-color: #fee2e2;
    color: #b91c1c;
    padding: 12px 16px;
    border-radius: 6px;
    border: 1px solid #fca5a5;
    margin-bottom: 16px;
    font-size: 0.95rem;
  }
  </style>
  