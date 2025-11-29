// Home.tsx
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { v4 as uuidv4 } from 'uuid';

export default function Home() {
  const [roomId, setRoomId] = useState('');
  const navigate = useNavigate();

  const createRoom = () => {
    const newRoom = uuidv4();
    navigate(`/room/${newRoom}`);
  };

  const joinRoom = () => {
    if (roomId.trim()) {
      navigate(`/room/${roomId}`);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-blue-900 flex items-center justify-center">
      <div className="bg-white/10 backdrop-blur-lg p-12 rounded-2xl shadow-2xl">
        <h1 className="text-5xl font-bold text-white mb-8 text-center">GrokMeet</h1>
        <div className="space-y-6">
          <button
            onClick={createRoom}
            className="w-full py-4 bg-purple-600 hover:bg-purple-700 text-white text-xl rounded-xl transition"
          >
            새 회의 시작
          </button>
          <div className="flex gap-3">
            <input
              type="text"
              placeholder="방 코드 입력"
              value={roomId}
              onChange={(e) => setRoomId(e.target.value)}
              className="flex-1 px-4 py-3 rounded-lg bg-white/20 text-white placeholder-gray-300"
              onKeyPress={(e) => e.key === 'Enter' && joinRoom()}
            />
            <button
              onClick={joinRoom}
              className="px-8 py-3 bg-blue-600 hover:bg-blue-700 rounded-lg text-white"
            >
              입장
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}