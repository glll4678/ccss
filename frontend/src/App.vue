<script setup lang="ts">
import { ref } from 'vue';

const query = ref('甜甜圈');
const errorMessage = ref('');
const results = ref<{ hak_hon: string; hak_pin_a: string; hak_pin_b: string; source: string; votes: number }[]>([]);
const voted = ref<boolean[]>([]);

const handleSearch = async () => {
  errorMessage.value = '';
  try {
    if (query.value !== '甜甜圈') {
      throw new Error('模擬錯誤');
    }
    const data = [
      { hak_hon: '甜圈麭', hak_pin_a: 'tiamˇ kianˊ pangˋ', hak_pin_b: 'tiam kienˋ pangˋ', source: 'A先生', votes: 0 },
      { hak_hon: '烰箍仔', hak_pin_a: 'poˇ kieuˊ eˋ', hak_pin_b: 'po kieuˋ eˊ', source: 'B先生', votes: 0 },
      { hak_hon: '手鈪粄', hak_pin_a: 'suˋ agˋ banˋ', hak_pin_b: 'shiuˊ ag banˊ', source: 'C先生', votes: 0 },
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
  <div lang="hak-Hani-TW">
    <main class="main-content">
      <h1>詞詞字字</h1>
      <h2><span class="lang-name">臺灣客語</span>群眾辭典</h2>
      <div class="search-box">
        <input
          type="text"
          placeholder="輸入華語詞彙"
          class="search-input"
          v-model="query"
        />
        <button class="search-button" @click="handleSearch">搜尋</button>
      </div>
      <p>
        網站吂完成，這下單淨係 Demo 定。<br>
        歡迎追蹤<a href="/" rel="noopener">「詞詞字字」面書專頁</a>。
      </p>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </main>
    <div class="card-container" v-if="results.length > 0">
      <div v-for="(item, index) in results" :key="index" class="card">
        <h3>{{ item.hak_hon }}</h3>
        <div class="tone-block">
          <div class="tone-label">四縣｜</div>
          <div class="tone-text">{{ item.hak_pin_a }}</div>
        </div>
        <div class="tone-block">
          <div class="tone-label">海陸｜</div>
          <div class="tone-text">{{ item.hak_pin_b }}</div>
        </div>
        <br />
        <p class="contributor">貢獻者｜{{ item.source }}</p>
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
        <input type="text" placeholder="輸入貢獻者名" class="card-input" />
        <button class="card-button" @click="handleSubmit">同意以 CC0 授權貢獻，送出！</button>
      </div>
    </div>
    <footer class="footer">
      <div>
        © 2025 詞詞字字
      </div>
    </footer>
  </div>
</template>