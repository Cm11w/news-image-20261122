# QA INDEPENDEN — news-image-20261122

**Pemeriksa:** subagent QA independen (bukan pembangun entri).
**Waktu pemeriksaan:** Minggu 22 Nov 2026 ~07:55 WIB.
**Entri:** `~/workspace/makefun/news-image-20261122-entry/` (draw_entry.py, entry.png, main.ts, README.md, LICENSE, research-22nov.md)
**Kit:** `~/workspace/makefun/news-image-20261122-kit/news-image-20261122-kit/` — deadline Senin 24 Nov 2026 07:00 WIB (2026-11-24T00:00:00Z, terverifikasi di competition.yaml).

## VERDICT: SIAP SUBMIT ✅

Tidak ada blocker. Semua pemeriksaan format, determinisme, visual, dan kebenaran-vs-riset lolos. Ada 4 catatan minor (bukan blocker) dan 1 caveat proses (refresh sebelum submit, keputusan parent) — lihat bawah.

---

## 1. FORMAT — LULUS

| Item | Hasil |
|---|---|
| Format | PNG (valid, dibaca PIL) |
| Dimensi | 1024 × 1024 px (sesuai batas kit: ≤ 1024×1024) |
| Mode | RGB |
| Ukuran | **137.288 byte** (< 1.048.576 byte / 1 MiB) |
| SHA-256 | `5e067badd2e6a0161b5e206553ab24e5f20c802ab29d647c60d90c36e6fe5b08` |

## 2. DETERMINISME — LULUS (byte-identik)

- `draw_entry.py` dijalankan 2× ke direktori temp terpisah (`/tmp/qa-run1`, `/tmp/qa-run2`): kedua output SHA-256 = `5e067badd2e6a0161b5e206553ab24e5f20c802ab29d647c60d90c36e6fe5b08`, `cmp` terhadap `entry.png` → **identik byte-per-byte** (2/2).
- `main.ts` dengan `MAKEFUN_OUTPUT_DIR=/tmp/qa-ts`: output SHA-256 sama, `cmp` → **identik**.
- Catatan: draw_entry.py punya guard overflow (abort bila teks meluber) dan check ASCII — keduanya tidak terpicu saat run QA (run sukses).

## 3. VISUAL — LULUS (dibaca langsung dari entry.png)

- Tidak ada teks terpotong, meluber keluar kartu, tumpang tindih, atau glyph rusak. Semua teks di dalam kartu masing-masing; footer satu baris utuh.
- Tanggal **"Sunday, November 22, 2026"** terbaca jelas di masthead (emas di atas navy).
- Kelima cerita terbaca lengkap dari gambar saja: lead COP31 + WAR + MIDDLE EAST + CYBER + MARKETS, masing-masing dengan tag, headline, dan body.
- Downscale ~300 px (`/tmp/qa-small300.png`): judul "WORLD NEWS", tanggal, dan headline kelima kartu tetap terbaca. Body text mengecil hingga sulit dibaca pada ukuran itu — wajar untuk layout koran 1024 px dan bukan cacat (headline + tanggal yang dibawa tetap legible).

## 4. KEBENARAN vs RISET — LULUS (semua klaim terverifikasi)

Tanggal diverifikasi dengan `date -d`: **22 Nov 2026 = Sunday** (WIB dan UTC).

| # | Klaim di gambar | vs research-22nov.md | Status |
|---|---|---|---|
| — | "Sunday, November 22, 2026" | 22 Nov 2026 memang Minggu | ✅ |
| — | Subline "as reported on Sunday" | Riset: peristiwa Sabtu yang dilaporkan Minggu dihitung berita 22 Nov; subline ini disyaratkan riset | ✅ |
| 1 | "COP31 deadlocked into Sunday with no deal in sight" | Riset: "deadlocked / no deal yet", jangan tulis "gagal" — gambar tidak menulis "gagal" | ✅ (lihat minor #1) |
| 1 | "ran past their Friday deadline with no final text" | Deadline Jumat terlewat, tidak ada teks final per Sabtu malam/Minggu dini hari | ✅ |
| 1 | "draft drops every mention of fossil fuels and a $120bn adaptation fund" | Draf kedua hapus semua penyebutan fosil + target $120 miliar/tahun pendanaan adaptasi | ✅ (lihat minor #2) |
| 1 | "About 130 countries want the fossil-fuel language restored" | "sekitar 130 negara" (koalisi longgar) | ✅ |
| 1 | "a large group marched on the presidency office on Saturday night" | "large group" berbaris ke kantor presidensi Sabtu malam | ✅ |
| 1 | "first COP to end with no deal since 2000" | Health Policy Watch: pertama sejak COP6 Den Haag 2000 | ✅ |
| 2 | "Zelensky calls Putin a 'killer'" | Kutipan Zelensky ke CNN, atribusi dijaga ("calls" + nama) | ✅ |
| 2 | "Russia fired 3 ballistic missiles and 148 drones overnight, Kyiv said" | IBTimes, per pelaporan Ukraina; atribusi "Kyiv said" ada | ✅ |
| 2 | "Ukraine hit a refinery at Ryazan" | Al Jazeera 21 Nov 18:02 UTC, kebakaran terverifikasi lewat footage | ✅ |
| 3 | "Israeli strike kills 3 in Gaza" / "Three people were killed in Gaza City on Saturday, the Gaza Health Ministry said" | Reuters 21 Nov: 3 tewas, Kementerian Kesehatan Gaza | ✅ |
| 3 | "Israel said it hit Islamic Jihad militants in a truck with a WCK logo; WCK said it was not its vehicle" | IDF klaim militan Islamic Jihad; WCK menyangkal afiliasi. Korban TIDAK disebut pekerja WCK atau militan tanpa atribusi | ✅ (lihat minor #4) |
| 4 | "FBI crime database hacked" (headline) / body: "investigating an apparent breach of its crime database, CNN reported" | "Apparent breach" menurut CNN; FBI belum konfirmasi publik | ✅ (lihat minor #3) |
| 4 | "its second breach in two months" | Pelanggaran kedua dalam beberapa bulan; September ShinyHunters → Nov ~2 bulan | ✅ |
| 4 | "Trump downplayed it on Saturday; it is unclear if data was stolen" | Trump meremehkan Sabtu 21 Nov (Fox News); belum diketahui apakah data dicuri | ✅ |
| 5 | "Bitcoin fell to $55,830 on Friday, its lowest since September 2024" | Reuters: $55.830 Jumat, terendah sejak Sep 2024 | ✅ |
| 5 | "as AI-stock fears spread" | Pemicu: kekhawatiran valuasi saham AI | ✅ |
| 5 | "It rose 8% on Saturday to about $59,950" | Reuters: naik >8% ke ~$59.952 Sabtu | ✅ (pembulatan wajar) |
| 5 | "after $2.4bn in futures were liquidated in a day" | CoinGlass via Binance: $2,4 miliar / 24 jam | ✅ |
| — | Footer "Sources: Reuters - AP - CNN - BBC - Al Jazeera" | Semua sumber itu dipakai di riset (AP via BytesEU; BBC via EuropeSays) | ✅ |
| — | Tidak ada klaim tanker Hormuz "Minggu", tidak ada Gempa Peru, tidak ada klaim basi lain | Sesuai bagian "DIPERTIMBANGKAN, TIDAK DIMASUKKAN" di riset | ✅ |

## 5. KIT CHECK PEMBANGUN — INTERPRETASI JUJUR ✅

Bukti dibaca: `/tmp/kitcheck-20261122.txt`. Klaim pembangun ("4 passed, 1 failed = transcripts_present, 14 skipped, 5 checked at submission") **cocok persis** dengan isi file — saya hitung ulang: pass = competition_open, snapshot, license_osi, entrypoint (4); FAIL = transcripts_present (1); skip = 14; at-submission = repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot (5).

- FAIL `transcripts_present` BUKAN cacat entri: itu langkah submit (bundle transkrip) yang memang menjadi tugas parent saat submit. Semua 14 skip adalah konsekuensi logis dari belum adanya transkrip.
- 5 cek "at submission" (repo publik, owner, repo dibuat setelah pembukaan, commit ter-push, snapshot tidak duplikat) masih harus dipenuhi saat submit — di luar lingkup entri ini.

---

## CATATAN MINOR (bukan blocker — tidak perlu perbaikan sebelum submit)

1. **Lead headline "no deal in sight"** — sedikit lebih kuat dari riset ("no deal yet"; kesepakatan masih mungkin tercapai Minggu siang/malam). Body kartu sendiri sudah akurat ("no final text"). Nuansa headline, bukan kesalahan faktual.
2. **"$120bn adaptation fund"** — riset menyebut target **$120 miliar per tahun**; gambar menghilangkan "per year". Bukan salah, tapi kurang presisi (bukan dana sekali bayar).
3. **Headline CYBER "FBI crime database hacked"** — tanpa kualifikasi di headline; body langsung mengoreksi dengan "apparent breach", "CNN reported", dan "unclear if data was stolen". Headline shorthand yang umum; aturan kejujuran riset (jangan klaim data dicuri) dipatuhi.
4. **MIDDLE EAST: "in a truck with a WCK logo"** — detail logo berasal dari saksi mata menurut riset, sedangkan klaim IDF adalah militan + makanan untuk anggota Islamic Jihad. Gambar menaruh detail logo di dalam klausa klaim Israel — kompresi minor; atribusi korban tetap benar (tidak disebut pekerja WCK / militan tanpa atribusi).

## CAVEAT PROSES (untuk keputusan parent, bukan temuan QA)

Riset bagian "REFRESH" menyatakan entri ini adalah **snapshot pagi** (~07:45 WIB; hari 22 Nov baru ~45 menit dalam UTC saat riset) dan **sangat merekomendasikan refresh** Senin 23 Nov ~07:00 WIB setelah 22 Nov berakhir UTC — terutama COP31 (kesepakatan/kegagalan resmi bisa pecah Minggu siang/malam) dan kemungkinan peristiwa besar siang 22 Nov menggeser Cerita 4/5. README entri juga menyatakan hal yang sama secara terbuka. Entri ini akurat sebagai snapshot pagi; apakah di-submit apa adanya atau di-refresh dulu adalah keputusan parent (deadline masih Senin 24 Nov 07:00 WIB, jadi ada waktu satu hari penuh setelah refresh).

---

## RINGKASAN BUKTI

- SHA-256 entry.png: `5e067badd2e6a0161b5e206553ab24e5f20c802ab29d647c60d90c36e6fe5b08`
- Ukuran: 137.288 byte; 1024×1024; RGB; PNG valid
- Determinisme: 2× draw_entry.py + 1× main.ts → semua byte-identik (`cmp` lolos)
- Visual: bersih, tanpa clipping/overlap; terbaca penuh; headline tetap terbaca di 300 px
- Kebenaran: semua angka/nama/atribusi cocok dengan research-22nov.md; 4 minor, 0 blocker
- Kit check: interpretasi pembangun jujur; satu-satunya FAIL adalah langkah submit (transkrip)
