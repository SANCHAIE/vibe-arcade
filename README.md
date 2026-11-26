# 🕹️ Vibe Arcade · Workshop 07

สนามรวมเกมจาก **Vibe Game Jam** · หน้าเว็บ: https://sanchaie.github.io/vibe-arcade/

## วิธีส่งเกมของทีม (Pull Request)
1. ใน repo นี้ กด **Add file → Create new file**
2. ตั้งชื่อไฟล์ `games/ชื่อทีมภาษาอังกฤษ.json` เช่น `games/team-crab.json`
   (GitHub จะ **Fork** repo ให้อัตโนมัติ)
3. วางข้อมูลนี้แล้วแก้เป็นของทีม:
   ```json
   {
     "team": "ชื่อทีม",
     "title": "ชื่อเกม",
     "emoji": "🎮",
     "description": "อธิบายเกม 1 บรรทัด",
     "play": "https://ชื่อผู้ใช้.github.io/ชื่อrepo/",
     "repo": "https://github.com/ชื่อผู้ใช้/ชื่อrepo"
   }
   ```
4. กด **Commit changes → Propose changes → Create pull request**
5. รอ CI ตรวจ (✅ ผ่าน / ❌ ไม่ผ่าน ให้กดดูว่าผิดตรงไหนแล้วแก้)
6. อาจารย์กด **Merge** แล้วเกมจะขึ้นจอใหญ่ภายในประมาณ 1 นาที 🎉

## สำหรับอาจารย์ (ตั้งค่าครั้งแรก)
- Settings → Pages → Source: **GitHub Actions**
- PR จากบัญชีใหม่ต้องกด **Approve and run** ก่อน CI จะทำงาน (ทำบนจอใหญ่ให้นักเรียนเห็นได้)
- ทดสอบในเครื่อง: `python3 scripts/build.py --out games.json` แล้วเปิด `index.html` ผ่าน local server
