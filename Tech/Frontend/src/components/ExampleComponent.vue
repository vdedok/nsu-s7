<template>
  <div>
    <h4>Оценка психологического состояния</h4>
    <p>Экипажей воздушных судов на основе анализа эмоциональной окраски речи</p>
    <div id="recorder">
      <div>
        <span>Записать пример общения в кабине или радиообмена:</span><br>
        <span>Рекомендуемая длительность не менее 10 секунд.</span><br>
        <button @click="startRecording" :disabled="isRecording">Start Recording</button>
        <button @click="stopRecording" :disabled="!isRecording">Stop Recording</button>
        <!-- <button @click="sendAudioToServer" :disabled="!audioUrl">Send Audio to Server</button> -->
        <audio v-if="audioUrl" :src="audioUrl" controls></audio>
      </div>
    </div>
    <span v-for="(elem, i) in data" :key="i">
    </span>
    <div id="container" style="height: 500px;"></div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'


const data = ref([[{'Emotion': 'anger', 'Score': '1.7'}, {'Emotion': 'disgust', 'Score': '62.2'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.1'}, {'Emotion': 'happiness', 'Score': '0.1'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '35.8'}], [{'Emotion': 'anger', 'Score': '5.1'}, {'Emotion': 'disgust', 'Score': '94.8'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.0'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '0.0'}], [{'Emotion': 'anger', 'Score': '2.7'}, {'Emotion': 'disgust', 'Score': '50.2'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.1'}, {'Emotion': 'happiness', 'Score': '0.1'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '46.9'}], [{'Emotion': 'anger', 'Score': '0.2'}, {'Emotion': 'disgust', 'Score': '36.1'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.0'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '63.6'}], [{'Emotion': 'anger', 'Score': '0.1'}, {'Emotion': 'disgust', 'Score': '99.9'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.0'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '0.0'}], [{'Emotion': 'anger', 'Score': '0.3'}, {'Emotion': 'disgust', 'Score': '99.7'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.0'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '0.0'}], [{'Emotion': 'anger', 'Score': '0.0'}, {'Emotion': 'disgust', 'Score': '100.0'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.0'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '0.0'}], [{'Emotion': 'anger', 'Score': '0.0'}, {'Emotion': 'disgust', 'Score': '100.0'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.0'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '0.0'}], [{'Emotion': 'anger', 'Score': '1.2'}, {'Emotion': 'disgust', 'Score': '96.1'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.0'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '2.6'}], [{'Emotion': 'anger', 'Score': '2.9'}, {'Emotion': 'disgust', 'Score': '57.1'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.1'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '39.8'}], [{'Emotion': 'anger', 'Score': '98.3'}, {'Emotion': 'disgust', 'Score': '1.6'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.0'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '0.0'}], [{'Emotion': 'anger', 'Score': '0.0'}, {'Emotion': 'disgust', 'Score': '100.0'}, {'Emotion': 'enthusiasm', 'Score': '0.0'}, {'Emotion': 'fear', 'Score': '0.0'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '0.0'}], [{'Emotion': 'anger', 'Score': '0.1'}, {'Emotion': 'disgust', 'Score': '68.6'}, {'Emotion': 'enthusiasm', 'Score': '0.1'}, {'Emotion': 'fear', 'Score': '0.1'}, {'Emotion': 'happiness', 'Score': '0.0'}, {'Emotion': 'neutral', 'Score': '0.0'}, {'Emotion': 'sadness', 'Score': '31.1'}]])

import * as echarts from 'echarts';
type EChartsOption = echarts.EChartsOption;

function calc_plot() {
  let option: EChartsOption;

  const timeline = <string[]>[]
  const anger = <number[]>[]
  const disgust = <number[]>[]
  const enthusiasm = <number[]>[]
    
  const fear = <number[]>[]
  const happiness = <number[]>[]
  const neutral = <number[]>[]
  const sadness = <number[]>[]

  for (const [i, step] of data.value.entries()) {
    timeline.push(10*i + 's')
    anger.push(Number(step.at(0)!.Score))
    disgust.push(Number(step.at(1)!.Score))
    enthusiasm.push(Number(step.at(2)!.Score))
    fear.push(Number(step.at(3)!.Score))
    happiness.push(Number(step.at(4)!.Score))
    neutral.push(Number(step.at(5)!.Score))
    sadness.push(Number(step.at(6)!.Score))
}

  // eslint-disable-next-line prefer-const
  option = {
    legend: {
      data: ['anger', 'disgust', 'enthusiasm', 'fear', 'happiness', 'neutral', 'sadness']
    },
    xAxis: {
      type: 'category',
      data: timeline
    },
    yAxis: { type: 'value' },
    series: [
      { name: 'anger', data: anger, type: 'line', smooth: true },
      { name: 'disgust', data: disgust, type: 'line', smooth: true },
      { name: 'enthusiasm', data: enthusiasm, type: 'line', smooth: true },
      { name: 'fear', data: fear, type: 'line', smooth: true },
      { name: 'happiness', data: happiness, type: 'line', smooth: true },
      { name: 'neutral', data: neutral, type: 'line', smooth: true },
      { name: 'sadness', data: sadness, type: 'line', smooth: true },
    ]
  };
  return option
}


let chartDom : HTMLElement
let myChart : echarts.ECharts

onMounted(()=>{
  chartDom = document.getElementById('container')!;
  myChart = echarts.init(chartDom);

  myChart.setOption(calc_plot());
})
  
  const isRecording = ref(false);
  const mediaRecorder = ref<MediaRecorder | null>(null);
  const audioChunks = ref<Blob[]>([]);
  const audioUrl = ref<string | null>(null);

  
  let audioBlob : Blob
  
  async function startRecording() {
    audioChunks.value = [];
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: { channelCount: 1, sampleRate: 16000 } });
      mediaRecorder.value = new MediaRecorder(stream);  
      mediaRecorder.value.ondataavailable = (event: BlobEvent) => {
        audioChunks.value.push(event.data);
      };
      mediaRecorder.value.onstop = async () => {
        audioBlob = new Blob(audioChunks.value, { type: 'audio/wav' });
        audioUrl.value = URL.createObjectURL(audioBlob);
        await sendAudioToServer()
      };
      mediaRecorder.value.start();
      isRecording.value = true;
    } catch (error) {
      console.error('Error accessing microphone:', error); 
    }
  }
  // eslint-disable-next-line @typescript-eslint/require-await
  async function stopRecording() {
    if (mediaRecorder.value) {
      mediaRecorder.value.stop();
      isRecording.value = false;
      // await sendAudioToServer()
    }
  }

const uploadStatus = ref<string | null>(null);
async function sendAudioToServer() {
  // if (!audioUrl.value) {
  //   console.error('No audio recorded yet.');
  //   return;
  // }

  const audioBlob = new Blob(audioChunks.value, { type: 'audio/wav' });
  const formData = new FormData();
  formData.append('file', audioBlob, 'recording.wav');

  try {
    const response = await fetch('http://localhost:8000/upload', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      uploadStatus.value = 'Audio uploaded successfully!';
      const res = await response.json()
      data.value = res
      myChart.setOption(calc_plot());
      
    } else {
      uploadStatus.value = 'Failed to upload audio.';
    }
  } catch (error) {
    console.error('Error uploading audio:', error);
    uploadStatus.value = 'Error uploading audio.';
  }
}

</script>

<style lang="scss">
#recorder {
  background-color: #ebebeb;
  border: 1px #555555 solid;
  border-radius: 5px;
}

h4 {
  padding: 0px;
  margin: 0px;
}

button {
    margin: 5px;
  }
</style>