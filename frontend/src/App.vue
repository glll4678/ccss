<script setup lang="ts">
import { ref } from 'vue';

const query = ref('麵包');
const errorMessage = ref('');
const results = ref<{ hak_hon: string; hak_pin_a: string; hak_pin_b: string; source: string; votes: number }[]>([]);

const handleSearch = async () => {
  errorMessage.value = '';
  try {
    if (query.value !== '麵包') {
      throw new Error('模擬錯誤');
    }
    const data = [
      { hak_hon: '麵包', hak_lo: 'mien-pâu', hak_pin_a: 'mien bauˊ', hak_pin_b: 'mien⁺ bauˋ', source: '教育部《臺灣客語辭典》', votes: 0 },
      { hak_hon: '胖', hak_lo: 'pháng', hak_pin_a: 'pangˋ', hak_pin_b: 'pangˋ', source: '行政院客家委員會《客語外來語》', votes: 0 },
      { hak_hon: '麥粉粄', hak_lo: 'ma̍k-fún-pân', hak_pin_a: 'mag funˋ banˊ', hak_pin_b: 'magˋ funˊ banˋ', source: '阿彥', votes: 0 },
    ];
    results.value = data;
  } catch (error) {
    errorMessage.value = '：）';
    results.value = [];
    console.error('搜尋失敗:', error);
  }
};

const handleSubmit = () => {
  alert('：）');
};

const vote = (index: number, delta: number) => {
  results.value[index].votes += delta;
};

import { onMounted } from 'vue';
onMounted(() => handleSearch());
</script>

<template>
  <div lang="hak-Hani-TW">
    <main class="main-content">
      <h1>詞詞字字</h1>
      <h2>臺灣客語群眾辭典</h2>
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
        【歡迎追蹤<a clss="link" href="//www.facebook.com/bpmfv.xyz" rel="noopener" target="_blank">「詞詞字字」面書</a>】
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
        <p class="contributor">出處｜{{ item.source }}</p>
        <br />
        <div class="vote-controls">
          <button class="vote-down" @click="vote(index, -1)">-1</button>
          <span>{{ item.votes }}</span>
          <button class="vote-up" @click="vote(index, 1)">+1</button>
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
        © 2025 <a clss="link" href="/" rel="noopener" target="_blank">詞詞字字 bpmfv.xyz</a>
      </div>
    </footer>
  </div>
</template>