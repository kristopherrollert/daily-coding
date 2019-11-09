// Package distconv perfroms conversions from various distance units
package distconv

import "fmt"

type Feet float64
type Meters float64

func (f Feet) String() string   { return fmt.Sprintf("%gft", f) }
func (m Meters) String() string { return fmt.Sprintf("%gm", m) }

func FToM(f Feet) Meters { return Meters(f / 3.2808) }
func MToF(m Meters) Feet { return Feet(m * 3.2808) }
