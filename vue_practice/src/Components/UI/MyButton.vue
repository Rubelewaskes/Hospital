<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "my-button",
};
</script>

<style scoped>
.btn {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}

.btn:active {
  background-color: #003f7f;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.btn:disabled {
  background-color: #cccccc;
  color: #666666;
  cursor: not-allowed;
  box-shadow: none;
}
</style>

