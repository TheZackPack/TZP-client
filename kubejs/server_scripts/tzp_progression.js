// TZP v1 — progression glue: MA supremium as a hard gate on late Mekanism dissolution (official mek_data shape).
// Almost Unified priorities: config/almostunified/unification/materials.json (dominant items per tag).
// See AGENTS.md — Integration spine.

ServerEvents.recipes((event) => {
  event.remove({ id: 'mekanism:chemical_dissolution_chamber' });
  event.custom({
    type: 'mekanism:mek_data',
    category: 'misc',
    key: {
      C: { tag: 'c:circuits/ultimate' },
      E: { item: 'mysticalagriculture:supremium_essence' },
      I: { tag: 'c:ingots/refined_obsidian' },
      T: { item: 'mekanism:basic_chemical_tank' },
      X: { item: 'mekanism:steel_casing' },
    },
    pattern: ['ITI', 'CXC', 'IEI'],
    result: { count: 1, id: 'mekanism:chemical_dissolution_chamber' },
  });
});
