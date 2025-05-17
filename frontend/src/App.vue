<script setup lang="ts">
import { ref } from 'vue';

const query = ref('甜甜圈');
const errorMessage = ref('');
const results = ref<{ title: string; tone1: string; tone2: string; contributor: string; votes: number }[]>([]);
const voted = ref<boolean[]>([]);

const handleSearch = async () => {
  errorMessage.value = '';
  try {
    if (query.value !== '甜甜圈') {
      throw new Error('模擬錯誤');
    }
    const data = [
      { title: '甜圈麭', tone1: 'tiam kienˋ pangˋ', tone2: 'tiamˇ kianˊ pangˋ', contributor: 'A先生', votes: 0 },
      { title: '烰箍仔', tone1: 'poˇ kieuˊ eˋ', tone2: 'po kieuˋ eˊ', contributor: 'B先生', votes: 0 },
      { title: '手鈪粄', tone1: 'suˋ agˋ banˋ', tone2: 'shiuˊ ag banˊ', contributor: 'C先生', votes: 0 },
    ];
    results.value = data;
    voted.value = new Array(data.length).fill(false);
  } catch (error) {
    errorMessage.value = '搜尋失敗！';
    results.value = [];
    console.error('搜尋失敗:', error);
  }
};

const handleSubmit = () => {
  alert('已送出！');
};

const vote = (index: number, delta: number) => {
  if (voted.value[index]) return;
  results.value[index].votes += delta;
  voted.value[index] = true;
};

import { onMounted } from 'vue';
onMounted(() => handleSearch());
</script>

<template>
  <div lang="hak-Hant-TW">
    <main class="main-content">
      <h1>詞詞字字</h1>
      <h2>群眾客語辭典</h2>
      <div class="search-box">
        <input
          type="text"
          placeholder="輸入華語詞彙"
          class="search-input"
          v-model="query"
        />
        <button class="search-button" @click="handleSearch">搜尋</button>
      </div>
      <p>DEMO用。目前淨做得搜尋「甜甜圈」</p>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </main>
    <div class="card-container" v-if="results.length > 0">
      <div v-for="(item, index) in results" :key="index" class="card">
        <h3>{{ item.title }}</h3>
        <div class="tone-block">
          <div class="tone-label">四縣｜</div>
          <div class="tone-text">{{ item.tone1 }}</div>
        </div>
        <div class="tone-block">
          <div class="tone-label">海陸｜</div>
          <div class="tone-text">{{ item.tone2 }}</div>
        </div>
        <br />
        <p class="contributor">貢獻者｜{{ item.contributor }}</p>
        <br />
        <div class="vote-controls">
          <button class="vote-down" @click="vote(index, -1)" :disabled="voted[index]">-1</button>
          <span>{{ item.votes }}</span>
          <button class="vote-up" @click="vote(index, 1)" :disabled="voted[index]">+1</button>
        </div>
      </div>
      <div class="card">
        <h3>𠊎會！</h3>
        <input type="text" placeholder="輸入客語漢字" class="card-input" />
        <input type="text" placeholder="輸入四縣拼音" class="card-input" />
        <input type="text" placeholder="輸入海陸拼音" class="card-input" />
        <input type="text" placeholder="輸入貢獻者名字" class="card-input" />
        <button class="card-button" @click="handleSubmit">同意以 CC0 授權貢獻，送出！</button>
      </div>
    </div>
    <footer class="footer">
      © 2025 詞詞字字
    </footer>
  </div>
</template>

<style scoped>
.main-content {
  padding: 2rem;
}

.main-content h1 {
  margin-bottom: 0.25rem;
}

.main-content h2 {
  margin-top: 0;
}

.search-box {
  display: flex;
  gap: 0.5rem;
  width: 100%;
  max-width: 500px;
  margin: 1rem auto 0;
  justify-content: center;
}

.search-input {
  padding: 0.5rem;
  font-size: 1rem;
  box-sizing: border-box;
  flex: 1;
  max-width: 180px;
}

.search-button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

.search-button:hover {
  background-color: #45a049;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
}

.card {
  background-color: white;
  border: 1px solid #ccc;
  padding: 1.5rem;
  width: 250px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  border-radius: 8px;
}

.card:last-child {
  background-color: #fff9db;
}

.card h3 {
  margin: 0 0 0.5rem;
  font-size: 1.5rem;
}

.card p {
  margin: 0;
}


.tone-block {
  display: flex;
}

.tone-label {
  width: 3rem;
  margin-left: 2rem;
  margin-right: 0.25rem;
  text-align: right;
}

.tone-text {
  flex: 1;
  text-align: left;
}

.contributor {
  font-size: 0.8rem;
  color: #444;
}

.card-input {
  width: 100%;
  padding: 0.5rem;
  margin: 0.15rem 0;
  box-sizing: border-box;
}

.card-button {
  padding: 0.5rem 1rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

.card-button:hover {
  background-color: #45a049;
}

.vote-controls {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.vote-controls span {
  font-size: 1.25rem;
  font-weight: bold;
  color: #007BFF;
}

.vote-controls button {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  cursor: pointer;
}

.footer {
  text-align: center;
  font-size: 0.875rem;
  color: #666;
  margin-top: 2rem;
  padding-bottom: 1rem;
}

.error-message {
  color: red;
  margin-top: 1rem;
}

:global(body) {
  background-color: #e6f2ff;
}

@media (max-width: 600px) {
  .main-content {
    padding: 1rem;
  }

  .search-box {
    flex-direction: row;
    align-items: stretch;
    flex-wrap: wrap;
  }
}

.vote-up {
  color: #28a745;
}

.vote-down {
  color: #dc3545;
}
</style>