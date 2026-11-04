"""Chinese UI strings for Playden (phase 1: chrome, buttons, statuses, settings).

Run from the repository root before the build: python3 scripts/localize-zh.py
Only exact C++ string literals listed here are replaced, so keys, paths and
log lines are untouched.
"""
from pathlib import Path

ZH = {
    " (Windows folder, caches)": "（Windows 文件夹、缓存）",
    " Playden tries again on the next check.": " Playden 会在下次检查时重试。",
    " d ago": " 天前",
    " free": " 空闲",
    " free of ": " / 共 ",
    " h ": " 小时 ",
    " h ago": " 小时前",
    " min": " 分钟",
    " min ago": " 分钟前",
    " of ": " / ",
    " played": " 已游玩",
    " reserved": " 已预留",
    " reserved · ": " 已预留 · ",
    " used by games": " 游戏占用",
    " used · ": " 已用 · ",
    " · Disconnected": " · 未连接",
    " · Off": " · 关",
    " · On": " · 开",
    ". Steam Cloud has saves this console doesn't; Sync now or Play brings them down.":
        "。Steam 云存档有本机没有的存档；点“立即同步”或“开始游戏”会下载。",
    "Account name and password": "账号名和密码",
    "Action": "操作",
    "All": "全部",
    "Approve the sign-in in the Steam Mobile app, or type its code instead.":
        "在 Steam 手机应用中批准登录，或改为输入验证码。",
    "Approve the sign-in when Steam asks you to.": "Steam 提示时批准登录。",
    "Approved · Loading library": "已批准 · 正在加载游戏库",
    "Approved · Syncing library": "已批准 · 正在同步游戏库",
    "Artwork loading": "正在加载封面",
    "Available": "可用",
    "Back": "返回",
    "Backspace": "退格",
    "Both changed since the last sync. Pick which saves to keep; saves replaced here are backed up first.":
        "上次同步后两边都有改动。请选择保留哪一份存档；被替换的存档会先备份。",
    "Broken · user rating": "差评 · 用户评分",
    "Browsing can continue without saving.": "可以继续浏览，不会保存。",
    "Cancel": "取消",
    "Cancel download": "取消下载",
    "Cancel move": "取消移动",
    "Cancel the move?": "取消移动？",
    "Capacity  ": "容量  ",
    "Challenge expired": "验证已过期",
    "Check your phone": "请查看手机",
    "Checking licenses": "正在检查授权",
    "Checking which installed files changed…": "正在检查已安装文件的变动…",
    "Checking your Steam licenses…": "正在检查 Steam 授权…",
    "Clear the search or choose another library view.": "清除搜索条件，或切换到其他游戏库视图。",
    "Close": "关闭",
    "Compatibility": "兼容性",
    "Confirm": "确认",
    "Connect Steam": "连接 Steam",
    "Connecting securely": "正在安全连接",
    "Connecting securely…": "正在安全连接…",
    "Connection failed": "连接失败",
    "Console drop folder": "主机投放文件夹",
    "Console storage": "主机存储",
    "Console storage is full · Retrying": "主机存储已满 · 正在重试",
    "Controller": "手柄",
    "Controller connected": "手柄已连接",
    "Controller disconnected": "手柄已断开",
    "Copied": "已复制",
    "Copying paused": "复制已暂停",
    "Deleting title": "正在删除标题",
    "Demo": "试玩版",
    "Description unavailable.": "暂无简介。",
    "Disconnected": "未连接",
    "Download": "下载",
    "Download paused": "下载已暂停",
    "Downloaded": "已下载",
    "Downloads": "下载",
    "Downloads and game preparation show here. Install a game from its details to start.":
        "下载和游戏准备会显示在这里。从游戏详情页安装游戏即可开始。",
    "Downloads and preparation": "下载与准备",
    "Drive disconnected": "驱动器已断开",
    "Enter text": "输入文字",
    "Extended storage": "扩展存储",
    "Failed": "失败",
    "Family": "家庭",
    "Favorite": "收藏",
    "Favorited": "已收藏",
    "Favorites": "收藏夹",
    "Files": "文件",
    "Filter": "筛选",
    "Free  ": "空闲  ",
    "Free space unavailable": "可用空间不可用",
    "Free space unknown": "可用空间未知",
    "Game": "游戏",
    "Game saves on this console": "本机游戏存档",
    "Game settings": "游戏设置",
    "Hidden": "隐藏",
    "Hide": "隐藏",
    "Home": "主页",
    "Import games": "导入游戏",
    "Imported": "已导入",
    "Install": "安装",
    "Installed": "已安装",
    "Installs to ": "安装到 ",
    "L1/R1 Jump": "L1/R1 跳转",
    "L2/R2 Read more · page ": "L2/R2 查看更多 · 第 ",
    "LAST PLAYED": "上次游玩",
    "Last played": "上次游玩",
    "Last sync": "上次同步",
    "Left stick": "左摇杆",
    "Less than an hour ago": "不到一小时前",
    "Library": "游戏库",
    "Loading your library…": "正在加载游戏库…",
    "Location": "位置",
    "Logs": "日志",
    "Logs unavailable": "日志不可用",
    "Manage ›": "管理 ›",
    "Matches Steam Cloud.": "与 Steam 云存档一致。",
    "More": "更多",
    "Move game": "移动游戏",
    "Never": "从不",
    "Never played": "从未游玩",
    "Never synced on this PS5, and both sides already have saves. Pick which to keep; the other side is backed up first.":
        "本机从未同步过，而两边都已有存档。请选择保留哪一份；另一份会先备份。",
    "New collection": "新建合集",
    "Newest change": "最新改动",
    "Next": "下一个",
    "No Steam Cloud": "无 Steam 云存档",
    "No games here": "这里没有游戏",
    "No log entries": "没有日志条目",
    "No write access": "无写入权限",
    "Not checked yet. Opening Saves or Sync now checks it.": "尚未检查。打开“存档”或点“立即同步”即可检查。",
    "Not installed": "未安装",
    "Not installed · ": "未安装 · ",
    "Nothing has been logged here yet.": "这里还没有任何日志。",
    "Nothing in the queue": "队列为空",
    "Notifications": "通知",
    "Off": "关",
    "Offline": "离线",
    "On": "开",
    "Open": "打开",
    "Options": "选项",
    "Options ": "选项 ",
    "Other data": "其他数据",
    "Paused": "已暂停",
    "Playable · user rating": "可玩 · 用户评分",
    "Playden is checking this game with Steam Cloud. Its actions come back when that is done; you can leave this page meanwhile.":
        "Playden 正在向 Steam 云存档核对这个游戏。核对完成后按钮会恢复；你可以先离开此页面。",
    "Playden sends your password to Steam, encrypted, and never saves it. It keeps Steam's sign-in token ":
        "Playden 会把密码加密后发送给 Steam，绝不保存。它保存 Steam 的登录令牌 ",
    "Playtime": "游玩时长",
    "Preparation": "准备",
    "Preparing": "正在准备",
    "Preparing QR code": "正在生成二维码",
    "Previous": "上一个",
    "Putting the new files in place… The game can be played once this finishes.":
        "正在放置新文件…完成后即可开始游戏。",
    "QR code expired": "二维码已过期",
    "QR code unavailable": "二维码不可用",
    "QR code unavailable · Retry connection": "二维码不可用 · 重试连接",
    "Queue": "队列",
    "Queued": "已排队",
    "Ready when you are.": "随时可以开始。",
    "Reconnect its drive": "重新连接驱动器",
    "Refresh to continue": "刷新以继续",
    "Refreshing library · focus preserved": "正在刷新游戏库 · 保持焦点",
    "Removal": "删除",
    "Removing from this PS5": "正在从本机移除",
    "Reserved  ": "已预留  ",
    "Reserved by queue  ": "队列预留  ",
    "Reserved space is part of the free space, set aside for the downloads still queued.":
        "预留空间是可用空间的一部分，留给仍在队列中的下载。",
    "Restoring your accounts": "正在恢复你的账号",
    "Restoring your accounts…": "正在恢复你的账号…",
    "Retry the connection": "重试连接",
    "Right stick": "右摇杆",
    "Root access is missing": "缺少 root 权限",
    "Saves": "存档",
    "Saves here were never synced with this Steam account. Confirm to upload them.":
        "这里的存档从未与该 Steam 账号同步过。确认后将上传。",
    "Saves here would replace the ones in Steam Cloud, and this PS5 hasn't uploaded any for this game before. If the game didn't show your progress, keep the Cloud saves. Either side is backed up first.":
        "这里的存档会覆盖 Steam 云存档，而本机从未为该游戏上传过存档。如果游戏里没显示你的进度，请保留云存档。两边都会先备份。",
    "Scan for the full release notes": "扫码查看完整更新说明",
    "Sections": "分区",
    "Select": "选择",
    "Session controls": "会话控制",
    "Setting up for this PS5": "正在为本机配置",
    "Settings": "设置",
    "Setup": "安装设置",
    "Show": "显示",
    "Sign in": "登录",
    "Sign-in approved": "登录已批准",
    "Signing in": "正在登录",
    "Signing out securely": "正在安全退出",
    "Size": "大小",
    "Sort": "排序",
    "Starting…": "正在开始…",
    "Steam Cloud": "Steam 云存档",
    "Steam Cloud has newer saves. They come down when you reinstall the game or press Sync now.":
        "Steam 云存档有更新的存档。重新安装游戏或点“立即同步”时会下载。",
    "Steam Family": "Steam 家庭",
    "Steam Guard": "Steam 令牌",
    "Steam asks for a code to confirm that it is you. Codes have five letters or digits.":
        "Steam 要求输入验证码以确认是你本人。验证码为五位字母或数字。",
    "Step 3 of 6 · Copying …": "第 3 步，共 6 步 · 正在复制 …",
    "Storage": "存储",
    "Storage disconnected": "存储已断开",
    "Storage is full": "存储已满",
    "Store": "商店",
    "The game may be running. Playden syncs its saves once it stops.":
        "游戏可能正在运行。游戏停止后 Playden 会同步存档。",
    "The game was uninstalled; its saves and settings were kept. ": "游戏已卸载；存档和设置已保留。 ",
    "This console": "本机",
    "This game doesn't use Steam Cloud. Its saves exist only on this PS5.":
        "该游戏不使用 Steam 云存档，存档只存在于本机。",
    "To ": "到 ",
    "Touchpad": "触摸板",
    "Transfer": "传输",
    "USB drive": "USB 驱动器",
    "USB drive 2": "USB 驱动器 2",
    "Uninstall": "卸载",
    "Uninstall games to sign in": "卸载游戏以登录",
    "Uninstalling": "正在卸载",
    "Unknown": "未知",
    "Untested": "未测试",
    "Update ": "更新 ",
    "Update anyway": "仍然更新",
    "Update anyway?": "仍然更新？",
    "Update paused": "更新已暂停",
    "Update queued": "更新已排队",
    "Updated": "已更新",
    "Used  ": "已用  ",
    "Used by games  ": "游戏占用  ",
    "Verification": "验证",
    "Waiting for Steam to check your account name and password.":
        "正在等待 Steam 校验账号名和密码。",
    "Waiting for a secure challenge…": "正在等待安全验证…",
    "Waiting for approval": "等待批准",
    "What's going on": "当前状态",
    "Will sync after play": "游玩后同步",
    "Works · user rating": "好评 · 用户评分",
    "YOUR GAMES": "你的游戏",
    "on this PS5 so you stay signed in.": "保存在本机，以便保持登录。",
    "only until you close Playden. You will sign in again next time.":
        "仅在关闭 Playden 前有效。下次需要重新登录。",
    # --- Home, Downloads, Manage ---
    "Try again": "重试",
    "Sync now": "立即同步",
    "downloads Cloud saves": " 下载云存档",
    "into the kept data": " 写入保留数据",
    "Remove leftover data…": "移除遗留数据…",
    " with saves": "（含存档）",
    "Delete saves on this console…": "删除本机存档…",
    "Cloud keeps its copy": "云端仍保留副本",
    "Nothing to do": "无需操作",
    "Cross Select": "× 选择",
    "Circle Back": "○ 返回",
    "None": "无",
    "Failed": "失败",
    "Unavailable": "不可用",
    "Ready": "就绪",
    "Ready — simulated": "就绪 — 模拟",
    "Checking": "检查中",
    "Connected": "已连接",
    # --- Settings ---
    "Account": "账号",
    "Cached library · Offline": "缓存的游戏库 · 离线",
    "Steam connected · Synced": "Steam 已连接 · 已同步",
    "Steam connected": "Steam 已连接",
    "Sign out…": "退出登录…",
    "Add Windows games from a drive or the console drop folder":
        "从驱动器或主机投放文件夹添加 Windows 游戏",
    " found": " 个已找到",
    "Store name in PS5 titles": "在 PS5 标题中显示商店名",
    "Sync Cloud saves automatically": "自动同步云存档",
    "Before Play, after each game and when Playden starts.":
        "开始游戏前、每局结束后以及 Playden 启动时。",
    "Off: saves move only when you choose Sync in Saves.":
        "关闭：仅在“存档”里选择同步时才传输。",
    "Library and storage": "游戏库与存储",
    "Games storage": "游戏存储",
    "Where new games are installed": "新游戏的安装位置",
    "Storage is unavailable": "存储不可用",
    "Manage installed games": "管理已安装游戏",
    "Update games, move them to another drive, or uninstall the ones you no longer play":
        "更新游戏、移动到其他驱动器，或卸载不再玩的游戏",
    " update": " 个更新",
    " updates": " 个更新",
    "Kept game data": "保留的游戏数据",
    "Saves and settings kept when a game is uninstalled": "卸载游戏时保留的存档和设置",
    "Leftover PS5 titles": "遗留的 PS5 标题",
    "Game titles Playden no longer has a record of": "Playden 已无记录的 PS5 标题",
    " title · ": " 个标题 · ",
    " titles · ": " 个标题 · ",
    "Unused game settings data": "未使用的游戏设置数据",
    " · Console storage": " · 主机存储",
    "Left by interrupted or finished preparations. Clean up removes only what no game is using.":
        "由中断或已完成的准备过程留下。清理只会删除没有游戏在用的部分。",
    "Runtime status": "运行库状态",
    "Games run through prospero-win": "游戏通过 prospero-win 运行",
    "Download language": "下载语言",
    "Used for new installs. A game without it falls back to English or its first language.":
        "用于新安装。游戏没有该语言时会退回英文或其第一语言。",
    "Downloads for slow networks": "慢速网络下载模式",
    "8 pieces at a time. Turn it off if downloads got slower.":
        "同时下载 8 个分片。如果下载变慢请关闭。",
    "Off: 4 pieces at a time. Turn it on if downloads stay near 1 MB/s.":
        "关闭：同时 4 个分片。如果速度一直在 1 MB/s 左右请打开。",
    "Download server": "下载服务器",
    "Steam default": "Steam 默认",
    "Fastest": "最快",
    "Uses the server Steam lists first.": "使用 Steam 列表中的第一台服务器。",
    "Tests the servers when a download starts and uses the fastest one.":
        "下载开始时测速，并使用最快的一台。",
    "Not offered on this network now. Steam default is used.":
        "当前网络未提供该服务器，将使用 Steam 默认。",
    "If it stops answering, Playden uses another one.": "如果它无响应，Playden 会改用其他服务器。",
    "Display": "显示",
    "Reduced motion": "减少动效",
    "Keep the focus ring; turn off scaling and transitions": "保留焦点框；关闭缩放和过渡动画",
    "Test the buttons and sticks": "测试按键和摇杆",
    "Updates": "更新",
    "Beta updates": "测试版更新",
    "Get test versions before they are released. They can have new bugs.":
        "在正式发布前获取测试版本，可能有新问题。",
    "Playden updates": "Playden 更新",
    "Checking…": "正在检查…",
    "Looking for a newer Playden on GitHub": "正在 GitHub 上查找新版 Playden",
    " available": " 可用",
    "Download ": "下载 ",
    "Working…": "处理中…",
    "Downloading Playden ": "正在下载 Playden ",
    "Unpacking Playden ": "正在解压 Playden ",
    " ready": " 已就绪",
    "Restart Playden to finish the update": "重启 Playden 以完成更新",
    "Check again": "重新检查",
    "Check now": "立即检查",
    "No newer update for version ": "已是最新版本 ",
    "Version ": "版本 ",
    "You have a beta": "你正在使用测试版",
    "Playden moves to the next stable version when it is out.":
        "正式版发布后 Playden 会自动切换到稳定版。",
    "Game updates": "游戏更新",
    "Checked": "已检查",
    "Checked ": "检查于 ",
    "Steam is checked once a day when you open it": "打开时每天检查一次 Steam",
    "No games installed": "没有已安装的游戏",
    "Checking ": "正在检查 ",
    "Couldn't check": "无法检查",
    "Steam didn't answer": "Steam 没有响应",
    " · last checked ": " · 上次检查 ",
    "Up to date": "已是最新",
    "Not checked": "未检查",
    "Runtime kit": "运行库",
    "The installed kit isn't the one this version was made for":
        "已安装的运行库与当前版本不匹配",
    "Needed to prepare and play games": "准备和运行游戏所需",
    "Looking for this version's kit on GitHub": "正在 GitHub 上查找此版本的运行库",
    "Downloading the runtime kit": "正在下载运行库",
    "Unpacking the runtime kit": "正在解压运行库",
}

FILES = [
    "src/homebrew/view.cpp",
    "src/homebrew/simulation.cpp",
    "src/homebrew/controller.cpp",
    "src/homebrew/host.cpp",
    "src/homebrew/library_controller.cpp",
]

total = 0
for name in FILES:
    path = Path(name)
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    original = text
    for en, zh in ZH.items():
        text = text.replace('"' + en + '"', '"' + zh + '"')
    if text != original:
        path.write_text(text, encoding="utf-8")
        total += 1
print(f"Localized {len(ZH)} strings across {total} files")

# Most drawing calls hand the renderer a Latin face directly, and a Latin face has no Han
# glyphs, so translated text came out as question marks. Route every text call in the view
# through a helper that first asks font_for() for a face that can draw the string.
view = Path("src/homebrew/view.cpp")
if view.exists():
    text = view.read_text(encoding="utf-8")
    if "zh_text(" in text:
        print("Text fallback already applied")
    else:
        anchor = (
            "            if (!preferred.font->has_glyph(codepoint) && cjk_.font != nullptr &&\n"
            "                cjk_.font->has_glyph(codepoint))\n"
            "                return cjk_;\n"
            "        }\n"
            "        return preferred;\n"
            "    }\n"
        )
        if anchor not in text:
            print("WARNING: font_for anchor missing; text keeps the Latin faces")
        else:
            text = text.replace("ui::text(", "zh_text(").replace("ui::paragraph(", "zh_paragraph(")
            helpers = (
                "\n"
                "    // Draw with the face that actually has this string's glyphs: translated labels the\n"
                "    // Latin faces cannot render would otherwise come out as question marks.\n"
                "    template <typename Target, typename... Rest>\n"
                "    void zh_text(Target &target, const ui::FontRef &face, std::string_view value, Rest... rest)\n"
                "    {\n"
                "        ui::text(target, font_for(value, face), value, rest...);\n"
                "    }\n"
                "\n"
                "    template <typename Target, typename... Rest>\n"
                "    void zh_paragraph(Target &target, const ui::FontRef &face, std::string_view value, Rest... rest)\n"
                "    {\n"
                "        ui::paragraph(target, font_for(value, face), value, rest...);\n"
                "    }\n"
            )
            text = text.replace(anchor, anchor + helpers, 1)
            view.write_text(text, encoding="utf-8")
            print("Routed the view's text calls through the fallback face")

# The CJK face is a pre-baked glyph atlas: characters missing from it draw as "?".
# Feed every non-ASCII character the translations use into the atlas the build bakes,
# by pointing the CJK font line at a catalog file that holds the original catalog text
# plus this build's characters.
chars = sorted({ch for value in ZH.values() for ch in value if ord(ch) > 0x7F})
catalog = Path("fixtures/ui-comparison/catalog.json")
if catalog.exists():
    combined = catalog.read_text(encoding="utf-8") + "".join(chars)
else:
    combined = "".join(chars)
Path("/tmp/zh-catalog.txt").write_text(combined, encoding="utf-8")

build = Path("scripts/build-homebrew.sh")
if build.exists():
    shell = build.read_text(encoding="utf-8")
    old = "NotoSansCJKsc-Regular.otf|noto-cjk-fallback.huifont|catalog-european"
    new = "NotoSansCJKsc-Regular.otf|noto-cjk-fallback.huifont|european,text=/tmp/zh-catalog.txt"
    if old in shell:
        build.write_text(shell.replace(old, new, 1), encoding="utf-8")
        print(f"Baking {len(chars)} extra characters into the CJK atlas")
    else:
        print("WARNING: CJK font line not found; the atlas keeps its old characters")
