<template>
  <header class="navbar">
    <div class="navbar-content">
      <h1 class="title">🎄 Wishmas List</h1>
      <button
        v-if="isLoggedIn"
        class="logout-btn"
        @click="logout"
      >
        Se déconnecter
      </button>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/lib/axios'

const isLoggedIn = ref(false)

onMounted(() => {
  isLoggedIn.value = !!localStorage.getItem('authToken')
})

const logout = async () => {
  try {
    await api.post('/api/logout/')
  } catch (err) {
    console.error('Erreur lors de la déconnexion :', err)
  } finally {
    localStorage.removeItem('authToken')
    isLoggedIn.value = false
    window.location.href = '/login'
  }
}
</script>

<style scoped>
.navbar {
  background-color: #2e3a59;
  color: white;
  padding: 1rem 2rem;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 10;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.title {
  font-size: 1.4rem;
  font-weight: bold;
  margin: 0;
}

.logout-btn {
  background-color: #ff4d4f;
  border: none;
  padding: 0.5rem 1rem;
  color: white;
  font-weight: bold;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.logout-btn:hover {
  background-color: #d9363e;
}
</style>
