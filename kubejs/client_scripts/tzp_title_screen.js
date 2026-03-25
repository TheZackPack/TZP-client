// Strip vanilla/NeoForge title icon buttons (small widgets) that FancyMenu often
// fails to match to mc_titlescreen_* identifiers — they then stay visible in the middle.
// Wide buttons (Singleplayer, copyright, etc.) are left alone.

const $Minecraft = Java.loadClass('net.minecraft.client.Minecraft')
const $TitleScreen = Java.loadClass('net.minecraft.client.gui.screens.TitleScreen')
const $AbstractWidget = Java.loadClass('net.minecraft.client.gui.components.AbstractWidget')

let __tzpTitleStripped = null

ClientEvents.tick(() => {
	const mc = $Minecraft.getInstance()
	if (!mc) return
	const screen = mc.screen
	if (!screen || !(screen instanceof $TitleScreen)) {
		__tzpTitleStripped = null
		return
	}
	if (__tzpTitleStripped === screen) return

	const list = screen.renderables
	const n = list.size()
	const toRemove = []
	for (let i = 0; i < n; i++) {
		const r = list.get(i)
		if (!(r instanceof $AbstractWidget)) continue
		const w = r
		const ww = w.getWidth()
		const hh = w.getHeight()
		if (ww > 0 && hh > 0 && ww <= 28 && hh <= 28) {
			toRemove.push(w)
		}
	}
	for (let j = 0; j < toRemove.length; j++) {
		screen.removeWidget(toRemove[j])
	}
	__tzpTitleStripped = screen
})
